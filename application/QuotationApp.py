import tkinter as tk
from tkinter import ttk
import matplotlib
from infrastructure.gateway.AweSomeAPIGateway import get_quotation_one_day
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
from infrastructure.db.dollarRepository import get_quotation_by_day
from infrastructure.db.dollarRepository import insert
from datetime import date
from datetime import timedelta
from infrastructure.service.QuotationDTO import QuotationDTO
from datetime import datetime as dt
from application.entities.CurrencyQuotationEntity import CurrencyQuotationEntity
from application.model.enum.Currencies import Currencies
from application.model.enum.QuotationType import QuotationType

matplotlib.use("TkAgg")
NUMBER_OF_DAYS = 10


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cotação')

        # criar uma figura
        self.figure = Figure(figsize=(15, 6), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # criar o gráfico
        self.chart = self.figure.add_subplot()
        self.showDollar()

        create_button(self, "Mostrar Gráfico do Dólar", self.showDollar)
        create_button(self, "Mostrar Gráfico do Euro", self.showEuro)
        create_button(self, "Mostrar Gráfico do Bitcoin", self.showBitcoin)

    def showDollar(self):
        plot_quotation(self, get_quotation(Currencies.DOLLAR))

    def showEuro(self):
        plot_quotation(self, get_quotation(Currencies.EURO))

    def showBitcoin(self):
        plot_quotation(self, get_quotation(Currencies.BITCOIN))


def create_button(self, text, command):
    return ttk.Button(self, text=text, command=command).pack(fill="x", side="left", expand=True, padx=5)


def plot_quotation(self, quotations_mapped):
    self.chart.clear()

    self.chart.plot(quotations_mapped.date_quotation, quotations_mapped.quotation_for_bid, marker='o', label='Compra')
    self.chart.plot(quotations_mapped.date_quotation, quotations_mapped.quotation_for_ask, marker='o', label='Venda')
    self.chart.plot(quotations_mapped.date_quotation, quotations_mapped.quotation_for_low, marker='o', label='Mínimo')
    self.chart.plot(quotations_mapped.date_quotation, quotations_mapped.quotation_for_high, marker='o', label='Máximo')

    self.chart.set_title(quotations_mapped.currency)
    self.chart.set_xlabel('Dias')
    self.chart.set_ylabel('BRL')
    self.chart.grid()
    self.chart.legend()

    self.figure_canvas.draw()


def get_quotation(currency: Currencies):
    quotationDTO = QuotationDTO(currency.name, [], [], [], [], [])

    last10Days = []
    for days in range(0, NUMBER_OF_DAYS):
        last10Days.append(date.today() - timedelta(days=days))

    for day in last10Days:
        if day.strftime('%A') == 'Saturday' or day.strftime('%A') == 'Sunday':
            continue

        quotationDB = get_quotation_by_day(currency.name.lower(), str(day))

        if len(quotationDB) > 0 and have_all_type(quotationDB):
            quotationDTO.date_quotation.insert(0, quotationDB[0][1].strftime('%d/%m/%Y'))
            quotationDTO.quotation_for_bid.insert(0, get_quotation_by_type(quotationDB, "COMPRA"))
            quotationDTO.quotation_for_ask.insert(0, get_quotation_by_type(quotationDB, "VENDA"))
            quotationDTO.quotation_for_low.insert(0, get_quotation_by_type(quotationDB, "MINIMO"))
            quotationDTO.quotation_for_high.insert(0, get_quotation_by_type(quotationDB, "MAXIMO"))

        else:
            response = get_quotation_one_day(currency.value, str(day.year), day.month, day.day).json()
            if len(response) < 1:
                continue
            else:
                response = response[0]
            timestamp = int(response['timestamp'])
            dateX = dt.utcfromtimestamp(timestamp).strftime('%d/%m/%Y')
            quotationDTO.date_quotation.insert(0, dateX)
            quotationDTO.quotation_for_bid.insert(0, float(response['bid']))
            quotationDTO.quotation_for_ask.insert(0, float(response['ask']))
            quotationDTO.quotation_for_low.insert(0, float(response['low']))
            quotationDTO.quotation_for_high.insert(0, float(response['high']))

            insert_new_quotation_DB(currency, response)

    return quotationDTO


def insert_new_quotation_DB(currency, response):
    for x in [['bid', QuotationType.COMPRA],
              ['ask', QuotationType.VENDA],
              ['low', QuotationType.MINIMO],
              ['high', QuotationType.MAXIMO]]:
        insert(
            CurrencyQuotationEntity(
                str(currency.name),
                str(dt.utcfromtimestamp(int(response['timestamp'])).strftime('%Y-%m-%d')),
                response[x[0]],
                x[1]
            )
        )


def have_all_type(quotation):
    hasCompra = False
    hasVenda = False
    hasMaximo = False
    hasMinimo = False

    for c in quotation:
        if c[3] == 'COMPRA':
            hasCompra = True
        elif c[3] == 'VENDA':
            hasVenda = True
        elif c[3] == 'MAXIMO':
            hasMaximo = True
        elif c[3] == 'MINIMO':
            hasMinimo = True

    return hasCompra and hasVenda and hasMinimo and hasMaximo


def get_quotation_by_type(quotations, typeQuotation):
    quotation = [quotation for quotation in quotations if quotation[3] == typeQuotation]
    return float(quotation[0][2])
