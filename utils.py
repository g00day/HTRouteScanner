from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from error.scanning_error import ScanningError


import requests


def get_URL_scheme(url: str):
    parsed_url = urlparse(url)
    return parsed_url.scheme


def get_routes(url_base: str, resp: requests.Response) -> list:
    """ This function gets the requests.Response  
        soupifise it and  
        parses all links provided on that page  
        and returns all routes passed in these links  
    """

    soup = BeautifulSoup(resp.text, 'html.parser')    # soupify the response
    links = soup.find_all('a')

    routes = []
    for link in links:
        href = link.get('href')
        if href:

            full_url = urljoin(url_base, href)

            if get_URL_scheme(url_base) != get_URL_scheme(full_url):
                # avoiding routes to foreign resources
                continue

            routes.append(full_url)

    return routes


def check_response_and_return_error(resp: requests.Response) -> ScanningError:
    if not resp.ok or resp.is_redirect:
        error = ScanningError(resp.status_code, resp)
        return error
