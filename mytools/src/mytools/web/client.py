import requests

DEFAULT_TIMEOUT = 10


class APIError(Exception):
    pass


def get_json(url, params=None, timeout=DEFAULT_TIMEOUT):
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise APIError(f"GET {url} 失敗：{e}") from e
    return resp.json()


class APIClient:
    def __init__(self, base_url, timeout=DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "mytools/0.1.0"

    def get(self, path, params=None):
        return self._request("GET", path, params=params)

    def post(self, path, data=None):
        return self._request("POST", path, json=data)

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
            resp.raise_for_status()
        except requests.RequestException as e:
            raise APIError(f"{method} {url} 失敗：{e}") from e
        return resp.json()

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
