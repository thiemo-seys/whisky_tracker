import requests

#default headers to include in requests, so we do not get flagged as bot(403 forbidden errors)
DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def _get_response_from_url(url, headers=DEFAULT_HEADERS):
    return requests.get(url, headers=headers)


def _parse_response_to_bytes(response):
    return response.content


def _parse_response_to_text(response):
    return response.text


def get_page_content(url):
    page_response = _get_response_from_url(url)
    return _parse_response_to_bytes(page_response)