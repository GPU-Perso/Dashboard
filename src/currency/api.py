import configparser
import pathlib
from datetime import date, timedelta
from pprint import pprint
from time import strftime

import requests

# API key management
config = configparser.ConfigParser()
file = pathlib.Path(__file__).parent/"settings.ini"
print(file)
print("/home/tomtom/formation-python/Projets/Dashboard/src/currency/settings.ini")
config.read(file)
config.read("/home/tomtom/formation-python/Projets/Dashboard/src/currency/settings.ini")
ACCESS_KEY = config.get("exchangeratesapi", "ACCESS_KEY")
BASE_URL = "http://api.exchangeratesapi.io/v1"

def get_rates(currencies, days=2):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    api_rates = {}
    d = start_date
    while d <= end_date:
        url = f"{BASE_URL}/{d}?access_key={ACCESS_KEY}&symbols={','.join(currencies)}&format=1"
        print(url)
        rsp = requests.get(url)
        if not rsp and not rsp.json():
            return False, False
        api_rates[d.strftime("%Y-%m-%d")] = rsp.json().get("rates")
        d += timedelta(days=1)

    pprint(api_rates)

    all_days = sorted(api_rates.keys())
    all_rates = {currency: [] for currency in currencies}

    for d in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[d].items()]

    return all_days, all_rates

if __name__ == '__main__':
    print(ACCESS_KEY)
    print(BASE_URL)

    currencies = ["CAD", "AUD"]
    days, rates = get_rates(currencies, 1)
    pprint(days)
    pprint(rates)