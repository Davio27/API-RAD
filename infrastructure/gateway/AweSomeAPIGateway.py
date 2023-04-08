import requests


def get_quotation():
    return requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/10")
