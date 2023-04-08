import requests


def get_quotation(currency, days):
    return requests.get(f"https://economia.awesomeapi.com.br/json/daily/{currency}-BRL/{days}")
