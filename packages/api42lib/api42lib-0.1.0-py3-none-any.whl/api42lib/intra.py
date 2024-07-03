import logging
import math
import os
import re
import time
from base64 import b64encode
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Dict, Optional

import requests
import yaml
from tqdm import tqdm

handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)8.8s] - %(module)10.10s.%(funcName)-15.15s  ||  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
handler.setFormatter(formatter)

LOG = logging.getLogger(__name__)
LOG.addHandler(handler)
LOG.setLevel(logging.WARNING)

V2_URL_PATTERN = r"^(https:\/\/api\.intra\.42\.fr|^(?!\/?v3\/|\/?freeze|\/?pace-system))(?!\/?v3\/|\/?freeze|\/?pace-system)(\/?(?:[a-zA-Z0-9_-]+\/?)*)$"
V3_URL_PATTERN = r"^(\/?(v3\/)?(freeze|pace-system)\/(v\d)\/([\w\-\/]*))$"


def _detect_v3(func) -> callable:
    def wrapper(self, url: str, headers: Optional[Dict] = None, **kwargs) -> callable:
        headers = headers or {}
        LOG.debug("======================================")
        if re.match(V2_URL_PATTERN, url):
            self.token = self.token_v2
            api_route = url.replace(self.token.endpoint, "").lstrip("/").lstrip("v2/")
            url = f"{self.token.endpoint}/{api_route}"
        else:
            self.token = self.token_v3
            if match := re.match(V3_URL_PATTERN, url):
                url = f"https://{match.group(3)}.42.fr/api/{match.group(4)}/{match.group(5)}"
            LOG.debug(f"Using {APIVersion.V3.value} token")
        return func(self, url, headers, **kwargs)

    return wrapper


class APIVersion(Enum):
    V2 = "v2"
    V3 = "v3"


@dataclass
class Token:
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    token_url: Optional[str] = None
    endpoint: Optional[str] = None
    scopes: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    api_version: Optional[APIVersion] = None
    is_v3: bool = False
    access_token: Optional[str] = None
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    refresh_expires_at: Optional[datetime] = None
    refresh_token: Optional[str] = None

    def __post_init__(self) -> None:
        self.is_v3 = self.api_version == APIVersion.V3

    def __set_token(self, res: Dict) -> None:
        now_utc = datetime.now(timezone.utc)
        self.access_token = res.get("access_token", self.access_token)
        self.created_at = now_utc
        self.expires_in = int(res.get("expires_in", 0))
        self.expires_at = self.created_at + timedelta(seconds=self.expires_in)
        self.refresh_token = res.get("refresh_token", self.refresh_token)
        self.refresh_expires_in = int(res.get("expires_in", 0))
        self.refresh_expires_at = now_utc + timedelta(seconds=self.refresh_expires_in)

    def __set_payload_v2(self) -> Dict:
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": self.scopes,
        }

    def __set_payload_v3(self) -> Dict:
        is_refresheable = self.refresh_token and self.refresh_expires_at > datetime.now(
            timezone.utc
        )
        if is_refresheable:
            return {"grant_type": "refresh_token", "refresh_token": self.refresh_token}
        return {
            "grant_type": "password",
            "username": self.login,
            "password": self.password,
        }

    def is_valid(self) -> bool:
        if self.access_token is None or self.expires_at is None:
            LOG.debug("⏳ No valid token found. Fetching new one")
            return False
        if self.expires_at < datetime.now(timezone.utc):
            LOG.debug(f"💀 Token {self.api_version.value} expired. Fetching new one")
            return False
        return True

    def request_token(self) -> None:
        payload = self.__set_payload_v3() if self.is_v3 else self.__set_payload_v2()
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": b"Basic "
            + b64encode(
                bytes(self.client_id + ":" + self.client_secret, encoding="utf-8")
            ),
        }

        LOG.debug(f"⏳ Attempting to get a {self.api_version.value} token")
        data = requests.post(self.token_url, headers=headers, data=payload).json()
        self.__set_token(data)
        LOG.debug(f"🔑 Got {self.api_version.value} token -> '{self.access_token:10.10}...'")


class IntraAPIClient:
    verify_requests = True
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(IntraAPIClient, cls).__new__(cls)
        return cls.__instance

    def __init__(self, config_path: Optional[str] = None, progress_bar: bool = True) -> None:
        """
        Initializes the IntraAPIClient instance.

        This method initializes the IntraAPIClient with the given configuration path and progress bar option. If the instance
        has not been initialized before, it loads the configuration from the specified path or the default path, creates tokens
        for API versions V2 and V3, and marks the instance as initialized.

        Parameters:
        - config_path (Optional[str]): The path to the configuration file. If None, the default path 'config.yml' in the current
        working directory is used.
        - progress_bar (bool): A flag to enable or disable the progress bar during operations.

        Raises:
        - FileNotFoundError: If the specified configuration file does not exist.
        """
        if not hasattr(self, '__initialized'):
            config = self.__load_config(config_path)
            config_v2 = config.get("intra", {}).get("v2", {})
            config_v3 = config.get("intra", {}).get("v3", {})
            self.progress_bar = progress_bar
            self.token: Optional[Token] = None
            self.token_v2 = self.__create_token(config_v2, api_version=APIVersion.V2)
            self.token_v3 = self.__create_token(config_v3, api_version=APIVersion.V3)
            self.__initialized = True


    def __load_config(self, config_file: Optional[str] = None) -> Dict:
        if not config_file:
            config_file = f"{os.environ.get('PWD', '')}/config.yml"
            LOG.debug(f"Using default config file: {config_file}")

        try:
            with open(config_file, "r") as cfg_stream:
                return yaml.load(cfg_stream, Loader=yaml.BaseLoader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {config_file}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing config file: {e}")

    def __create_token(self, config: Dict, api_version: Optional[APIVersion] = None) -> Token:
        return Token(
            client_id=config.get("client", None),
            client_secret=config.get("secret", None),
            token_url=config.get("uri", None),
            scopes=config.get("scopes", None),
            login=config.get("login", None),
            password=config.get("password", None),
            endpoint=config.get("endpoint", None),
            api_version=api_version,
        )

    def __add_auth_header(self, headers: Optional[Dict] = None) -> Dict:
        if not headers:
            headers = {}
        headers["Authorization"] = f"Bearer {self.token.access_token}"
        return headers

    def __request(self, method: callable, url: str, headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        LOG.debug(f"=====> API {self.token.api_version.value} Request")
        if not self.token or not self.token.is_valid():
            self.token.request_token()

        tries = 0
        while True:
            LOG.debug(f"⏳ Attempting a {method.__name__.upper()} request to {url}")
            res = method(
                url,
                headers=self.__add_auth_header(headers),
                verify=self.verify_requests,
                **kwargs,
            )

            if res.status_code == 401:
                if tries < 5:
                    LOG.debug("💀 Token expired")
                    self.token.request_token()
                    tries += 1
                    continue
                else:
                    LOG.error("❌ Tried to renew token too many times, something's wrong")

            elif res.status_code == 404:
                raise ValueError(f"Invalid URL: {url}")

            elif res.status_code == 429:
                LOG.info(f"🚔 Rate limit exceeded - Waiting {res.headers['Retry-After']}s before requesting again")
                time.sleep(float(res.headers["Retry-After"]))
                continue

            if res.status_code >= 400:
                req_data = "{}{}".format(
                    url,
                    "\n" + str(kwargs["params"]) if "params" in kwargs.keys() else "",
                )
                error_origin = "Client" if res.status_code < 500 else "Server"
                raise ValueError(f"\n{res.headers}\n\n{error_origin}Error. Error {str(res.status_code)}\n{str(res.content)}\n{req_data}")

            LOG.debug(f"✅ Request returned with code {res.status_code}")
            return res

    @_detect_v3
    def get(self, url: str, headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self.__request(requests.get, url, headers, **kwargs)

    @_detect_v3
    def post(self, url: str, headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self.__request(requests.post, url, headers, **kwargs)

    @_detect_v3
    def patch(self, url: str, headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self.__request(requests.patch, url, headers, **kwargs)

    @_detect_v3
    def put(self, url: str, headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self.__request(requests.put, url, headers, **kwargs)

    @_detect_v3
    def delete(self, url: str, headers: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self.__request(requests.delete, url, headers, **kwargs)

    def pages(self, url: str, headers: Optional[Dict] = None, **kwargs) -> list:
        """
        Fetches all pages of data sequentially.

        This method sequentially fetches pages of data from a specified URL until all pages have been retrieved. It handles pagination automatically based on the API version being used (V2 or V3) and appends the results to a list which is then returned.

        Parameters:
        - url (str): The URL from which to fetch the data.
        - headers (Optional[Dict]): Optional HTTP headers to send with the request. Default is None.

        Keyword Args:
        - Any additional keyword arguments are passed directly to the `get` method.

        Returns:
        - List[Any]: A list of items fetched from all the pages.

        Note:
        - This method is suitable for fetching data when the total number of pages is manageable without concurrent requests.
        """

        headers = headers or {}
        kwargs["params"] = kwargs.get("params", {}).copy()
        kwargs["params"]["page"] = int(kwargs["params"].get("page", 1))
        kwargs["params"]["per_page"] = kwargs["params"].get("per_page", 100)

        res = self.get(url=url, headers=headers, **kwargs)
        if self.token.api_version == APIVersion.V2:
            items = res.json()
            if "X-Total" not in res.headers:
                return items
            initial_page = int(res.headers.get("X-Page", 1))
            total_pages = math.ceil(int(res.headers.get("X-Total", 1)) / int(res.headers.get("X-Per-Page", 1)))
        elif self.token.api_version == APIVersion.V3:
            data = res.json()
            items = data.get("items", [])
            initial_page = data.get("page", 1)
            total_pages = data.get("pages", 1)

        for page in tqdm(
            range(initial_page + 1, total_pages + 1),
            initial=1,
            total=total_pages,
            desc=url,
            unit="page",
            disable=not self.progress_bar,
        ):
            LOG.debug(f"Fetching page: {page}/{total_pages}")
            kwargs["params"] = kwargs.get("params", {})
            kwargs["params"]["page"] = page
            data = self.get(url=url, headers=headers, **kwargs).json()
            if self.token.api_version == APIVersion.V2:
                items.extend(data)
            elif self.token.api_version == APIVersion.V3:
                items.extend(data.get("items", []))

        return items

    def pages_threaded(self, url: str, headers: Optional[Dict] = None, stop_page: Optional[int] = None, threads: int = 0, thread_timeout: int = 15, **kwargs) -> list:
        """
        Fetches pages of data concurrently using multiple threads.

        This method fetches pages of data from a specified URL concurrently using a specified number of threads. It is designed to efficiently fetch large datasets by dividing the work across multiple threads. The method first fetches the initial page to determine the total number of items and calculates the total number of pages based on the 'per_page' parameter. It then fetches each page in a separate thread.

        Parameters:
        - url (str): The URL from which to fetch the data.
        - headers (Optional[Dict]): Optional HTTP headers to send with the request. Default is None.
        - stop_page (Optional[int]): The page number at which to stop fetching. If None, all pages will be fetched. Default is None.
        - threads (int): The number of threads to use for concurrent requests. If <= 0, the method will calculate the number of threads based on the number of CPU cores. Default is 0.
        - thread_timeout (int): The maximum number of seconds to wait for each thread to complete. Default is 15.

        Keyword Args:
        - Any additional keyword arguments are passed directly to the `get` method.

        Returns:
        - list: A list of items fetched from the pages.

        Note:
        - This method is suitable for fetching data when the total number of pages is large and fetching them sequentially would be inefficient.
        """
        headers = headers or {}
        kwargs["params"] = kwargs.get("params", {}).copy()
        kwargs["params"]["page"] = int(kwargs["params"].get("page", 1))
        kwargs["params"]["per_page"] = kwargs["params"].get("per_page", 100)

        def _page_thread(page: int) -> list:
            local_kwargs = deepcopy(kwargs)
            local_kwargs["params"]["page"] = page
            try:
                res = self.get(url=url, headers=headers, **local_kwargs)
                return res.json()
            except Exception as e:
                LOG.error(f"Error fetching page {page}: {e}")
                return []

        res = self.get(url=url, headers=headers, **kwargs)
        if self.token.api_version == APIVersion.V2:
            items = res.json()
            total_items = int(res.headers.get("X-Total", 0))
            per_page = int(res.headers.get("X-Per-Page", 30))
            total_pages = math.ceil(total_items / per_page)
        elif self.token.api_version == APIVersion.V3:
            data = res.json()
            total_pages = data.get("pages", 1)
            items = data.get("items", [])

        if stop_page:
            total_pages = min(total_pages, stop_page)

        if threads <= 0:
            threads = os.cpu_count() * 3

        LOG.debug(f"💻 Using {threads} threads")
        with tqdm(
            total=total_pages,
            initial=1,
            desc=url,
            unit="page",
            disable=not self.progress_bar,
        ) as pbar:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                future_to_page = {executor.submit(_page_thread, page): page for page in range(2, total_pages + 1)}

                for future in as_completed(future_to_page):
                    page = future_to_page[future]
                    try:
                        result = future.result(timeout=thread_timeout)
                        if self.token.api_version == APIVersion.V2:
                            items.extend(result)
                        elif self.token.api_version == APIVersion.V3:
                            items.extend(result.get("items", []))
                    except Exception as exc:
                        LOG.error(f"Page {page} generated an exception: {exc}")
                    pbar.update()

        return items

    def progress_bar_disable(self) -> None:
        """
        Disables the progress bar.

        This method sets the progress bar flag to False, effectively disabling the progress bar for any operations that are performed after this method is called.
        """
        self.progress_bar = False

    def progress_bar_enable(self) -> None:
        """
        Enables the progress bar.

        This method sets the progress bar flag to True, allowing the progress bar to be displayed for any operations that are performed after this method is called.
        """
        self.progress_bar = True
