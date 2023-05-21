import requests
from application.model.enum.Currencies import Currencies


def get_quotation_gateway(currency, days):
    return requests.get(f"https://economia.awesomeapi.com.br/json/daily/{currency}-BRL/{days}")


def get_quotation_one_day(currency: Currencies, year, month, day):
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)

    date = year + str(month) + str(day)
    return requests.get(f"https://economia.awesomeapi.com.br/json/daily/{currency}-BRL/?start_date={date}&end_date={date}")
