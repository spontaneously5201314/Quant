import requests
import json

url = "https://www.lixinger.com/api/open/a/stock/fundamental-info"


def get_pepb(url):
    payload = {
        'token': '9626c99d-ccf9-4f53-ae4d-fde228dd3442',
        "date": "2018-01-19",
        "metrics": ["pe_ttm", "market_value"],
        "stockCodes": ["000028", "600511"]
    }
    resp = requests.post(url, data=payload)
    content = resp.text
    print(content)


if __name__ == '__main__':
    get_pepb(url)
