import tkinter as tk
from tkinter import ttk
import matplotlib
from datetime import datetime as dt
from infrastructure.gateway.AweSomeAPIGateway import get_quotation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
from application.mapper import QuotationMapper

matplotlib.use("TkAgg")
NUMBER_OF_DAYS = 10
BITCOIN = 'BTC'
DOLLAR = 'USD'
EURO = 'EUR'


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

        self.cmdExecutardolar()

        create_button(self, "Mostrar Gráfico do Dólar", self.cmdExecutardolar)
        create_button(self, "Mostrar Gráfico do Euro", self.cmdExecutareuro)
        create_button(self, "Mostrar Gráfico do Bitcoin", self.cmdExecutarbit)

    def cmdExecutardolar(self):

        quotations = get_quotation(DOLLAR, NUMBER_OF_DAYS)
        quotationMapped = QuotationMapper.to_quotation_DTO(quotations)

        self.chart.clear()

        self.chart.plot(quotationMapped.xData_dolar, quotationMapped.yData_dolar, marker='o', label='Compra')
        self.chart.plot(quotationMapped.xData_dolar, quotationMapped.yData2_dolar, marker='o', label='Venda')
        self.chart.plot(quotationMapped.xData_dolar, quotationMapped.yData3_dolar, marker='o', label='Mínimo')
        self.chart.plot(quotationMapped.xData_dolar, quotationMapped.yData4_dolar, marker='o', label='Máximo')

        self.chart.set_title("Dolar")
        self.chart.set_xlabel('Dias')
        self.chart.set_ylabel('BRL')
        self.chart.grid()
        self.chart.legend()

        self.figure_canvas.draw()

    def cmdExecutareuro(self):

        # # Obter os dados do gráfico do euro
        # # https://economia.awesomeapi.com.br/json/daily/EUR-BRL/10

        quotation = get_quotation(EURO, NUMBER_OF_DAYS)
        xData_euro = []
        yData_euro = []
        yData2_euro = []
        yData3_euro = []
        yData4_euro = []

        for x in quotation.json():
            ts = int(x['timestamp'])
            xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData_euro.insert(0, xEixo)
            yData_euro.insert(0, float(x['bid']))
            yData2_euro.insert(0, float(x['ask']))
            yData3_euro.insert(0, float(x['low']))
            yData4_euro.insert(0, float(x['high']))

            # def plot_chart(self, title):

            self.chart.clear()

            self.chart.plot(xData_euro, yData_euro, marker='o', label='compra')
            self.chart.plot(xData_euro, yData2_euro, marker='o', label='venda')
            self.chart.plot(xData_euro, yData3_euro, marker='o', label='mínimo')
            self.chart.plot(xData_euro, yData4_euro, marker='o', label='máximo')

            self.chart.set_title("Euro")
            self.chart.set_xlabel('Quantidade de Dias')
            self.chart.set_ylabel('BRL')
            self.chart.grid()
            self.chart.legend()

            self.figure_canvas.draw()

    def cmdExecutarbit(self):

        # Obter os dados do gráfico do bitcoin
        # https://economia.awesomeapi.com.br/json/daily/EUR-BRL/10

        quotation = get_quotation(BITCOIN, NUMBER_OF_DAYS)

        xData_bitcoin = []
        yData_bitcoin = []
        yData2_bitcoin = []
        yData3_bitcoin = []
        yData4_bitcoin = []

        for x in quotation.json():
            ts = int(x['timestamp'])
            xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData_bitcoin.insert(0, xEixo)
            yData_bitcoin.insert(0, float(x['bid']))
            yData2_bitcoin.insert(0, float(x['ask']))
            yData3_bitcoin.insert(0, float(x['low']))
            yData4_bitcoin.insert(0, float(x['high']))

            # def plot_chart(self, title):
            self.chart.clear()

            self.chart.plot(xData_bitcoin, yData_bitcoin, marker='o', label='compra')
            self.chart.plot(xData_bitcoin, yData2_bitcoin, marker='o', label='venda')
            self.chart.plot(xData_bitcoin, yData3_bitcoin, marker='o', label='mínimo')
            self.chart.plot(xData_bitcoin, yData4_bitcoin, marker='o', label='máximo')
            self.chart.set_title("Bitcon")
            self.chart.set_xlabel('Quantidade de Dias')
            self.chart.set_ylabel('BRL')
            self.chart.grid()
            self.chart.legend()
            self.figure_canvas.draw()


def create_button(self, text, command):
    return ttk.Button(self, text=text, command=command).pack(fill="x", side="left", expand=True, padx=5)
