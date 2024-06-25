import requests
from urllib.parse import urljoin, urlparse, urlunparse
from typing import Dict, Any, List

BRIGHT_NETWORK_API_ROOT = "https://bn-hiring-challenge.fly.dev"

def _get_full_url(url: str):
    url = urljoin(BRIGHT_NETWORK_API_ROOT, url)
    parsed_url = urlparse(url)
    return urlunparse(parsed_url)

def _get(url: str) -> List[Dict[str, Any]]:
    full_url = _get_full_url(url)
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return []

def get_jobs() -> List[Dict[str, str]]:
    return _get("/jobs.json")

def get_members() -> List[Dict[str, str]]:
    return _get("/members.json")
