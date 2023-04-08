import tkinter as tk
from tkinter import ttk
import matplotlib
from infrastructure.gateway.AweSomeAPIGateway import get_quotation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
from application.mapper import QuotationMapper
from application.model.enum.Currencies import Currencies

matplotlib.use("TkAgg")
NUMBER_OF_DAYS = 10


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cotação')

        # APARENTEMENTE ESSE TRECHO DE CODE NÃO ESTÁ FAZENDO NADA
        # obtem img, converte img p/ objeto tkinter, cria widget Label c/ imagem e exibe na janela
        # image = Image.open('asset/image/background.png')
        # photo = ImageTk.PhotoImage(image)
        # label = tk.Label(self, image=photo)
        # label.place(x=0, y=0, relwidth=1, relheight=1)

        # criar uma figura
        self.figure = Figure(figsize=(15, 6), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # ESSE AQUI PARECE NÃO FAZER NADA TAMBEM
        # criar a barra de ferramentas
        # NavigationToolbar2Tk(self.figure_canvas, self)

        # criar o gráfico
        self.chart = self.figure.add_subplot()

        self.showDollar()

        create_button(self, "Mostrar Gráfico do Dólar", self.showDollar)
        create_button(self, "Mostrar Gráfico do Euro", self.showEuro)
        create_button(self, "Mostrar Gráfico do Bitcoin", self.showBitcoin)

    def showDollar(self, currency: Currencies = Currencies.DOLLAR):

        quotations = get_quotation(currency.value, NUMBER_OF_DAYS)
        quotations_mapped = QuotationMapper.to_DTO(quotations)

        plot_quotation(self, quotations_mapped)

    def showEuro(self, currency: Currencies = Currencies.EURO):

        quotations = get_quotation(currency.value, NUMBER_OF_DAYS)
        quotations_mapped = QuotationMapper.to_DTO(quotations)

        plot_quotation(self, quotations_mapped)

    def showBitcoin(self, currency: Currencies = Currencies.BITCOIN):

        quotations = get_quotation(currency.value, NUMBER_OF_DAYS)
        quotations_mapped = QuotationMapper.to_DTO(quotations)

        plot_quotation(self, quotations_mapped)


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
