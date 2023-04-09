
import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib
# import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import datetime as dt

matplotlib.use("TkAgg")


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x1000")
        self.title('API Cotação')
        
        
        
        
        # # Carregue a imagem
        # image = Image.open('C:\\Users\\davic\\OneDrive\\Documentos\\main project\\examples\\bg_gradient.jpg')
        
        # # Converta a imagem em um objeto de imagem tkinter
        # photo = ImageTk.PhotoImage(image)
        
        # # Crie um widget Label com a imagem e coloque-o na janela
        # self.label = tk.Label(self, image=photo)
        # self.label.image = photo
        # self.label.place(x=0, y=0)

        # criar uma figura
        self.figure = Figure(figsize=(15, 6), dpi=100)

        # crirar um objeto FigureCanvasTkAgg
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        # criar a barra de ferramentas
        NavigationToolbar2Tk(self.figure_canvas, self)

        # criar o gráfico
        self.chart = self.figure.add_subplot()

        self.current_value = tk.StringVar(value=10)

        self.cmdExecutardolar()
        self.cmdExecutareuro()
        self.cmdExecutarbit()

        self.figure_canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)
        
        
        # Criar parâmetro de entrada dos dias
        
        # Entrada 1
        
        self.spinRange = ctk.CTkOptionMenu(self, values=["10","15","20","25", "30", "35", "40", "45"], 
                                           variable=self.current_value)
        self.spinRange.font_color = "red"
        self.spinRange.pack(fill="x", side="left", expand=True, padx=5)
        
        
        # Entrada 2
        
        # self.spinRange = ctk.CTkEntry(self,placeholder_text="Digite a Quantidade de Dias", text_color=("red10", "#D90D10"), 
        #                               textvariable=self.current_value)
        # self.spinRange.font_color = "red"
        # self.spinRange.pack(fill="x", side="left", expand=True, padx=5)
        

        # self.spinRange = ttk.Spinbox(self, from_=1, to=60, textvariable=self.current_value,
        #     wrap=True,
        #     font=("Arial 18 bold")
        # )
        # self.spinRange.pack(fill="x", side="left", expand=True, padx=5)

        # Botão para atualizar o gráfico
        
        butãodolar = ctk.CTkButton(self, text="Mostrar Gráfico do Dólar", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.cmdExecutardolar)
        butãodolar.pack( fill="x", side="left", expand=True, padx=5)
        butãoeuro = ctk.CTkButton(self, text="Mostrar Gráfico do Euro", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.cmdExecutareuro)
        butãoeuro.pack(fill="x", side="left", expand=True, padx=5)
        butãobit = ctk.CTkButton(self, text="Mostrar Gráfico do Bitcoin", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.cmdExecutarbit)
        butãobit.pack(fill="x", side="left", expand=True, padx=5)

    # Criar funções para os botões

    def cmdExecutardolar(self):
        
        # Obter os dados do gráfico do dólar
        

        cotacoes_dolar = requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{self.current_value.get()}")
        xData_dolar = []
        yData_dolar = []
        yData2_dolar = []
        yData3_dolar = []
        yData4_dolar = []

        for x in cotacoes_dolar.json():
            ts = int(x['timestamp'])
            xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData_dolar.insert(0, xEixo)
            yData_dolar.insert(0, float(x['bid']))
            yData2_dolar.insert(0, float(x['ask']))
            yData3_dolar.insert(0, float(x['low']))
            yData4_dolar.insert(0, float(x['high']))
            
        
            
            self.chart.clear()
            self.chart.plot(xData_dolar, yData_dolar, marker = 'o', label='compra')
            self.chart.plot(xData_dolar, yData2_dolar, marker = 'o', label='venda')
            self.chart.plot(xData_dolar, yData3_dolar, marker = 'o', label='mínimo')
            self.chart.plot(xData_dolar, yData4_dolar, marker = 'o', label='máximo')
            self.chart.set_title("Dolar")
            self.chart.set_xlabel('Quantidade de Dias')
            self.chart.set_ylabel('BRL')
            self.chart.grid()
            self.chart.legend()
            self.figure_canvas.draw()
            
    def cmdExecutareuro(self):
        
        # # Obter os dados do gráfico do euro
        

        cotacoes_euro = requests.get(f"https://economia.awesomeapi.com.br/json/daily/EUR-BRL/{self.current_value.get()}")
        xData_euro = []
        yData_euro = []
        yData2_euro = []
        yData3_euro = []
        yData4_euro = []
        
        for x in cotacoes_euro.json():
            ts = int(x['timestamp'])
            xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData_euro.insert(0, xEixo)
            yData_euro.insert(0, float(x['bid']))
            yData2_euro.insert(0, float(x['ask']))
            yData3_euro.insert(0, float(x['low']))
            yData4_euro.insert(0, float(x['high']))
            
       
            
            self.chart.clear()
            self.chart.plot(xData_euro, yData_euro, marker = 'o', label='compra')
            self.chart.plot(xData_euro, yData2_euro, marker = 'o', label='venda')
            self.chart.plot(xData_euro, yData3_euro, marker = 'o', label='mínimo')
            self.chart.plot(xData_euro, yData4_euro, marker = 'o', label='máximo')
            self.chart.set_title("Euro")
            self.chart.set_xlabel('Quantidade de Dias')
            self.chart.set_ylabel('BRL')
            self.chart.grid()
            self.chart.legend()
            self.figure_canvas.draw()
            
        
        
    def cmdExecutarbit(self):
        
        # Obter os dados do gráfico do bitcoin
        
        cotacoes_bitcoin = requests.get(f"https://economia.awesomeapi.com.br/json/daily/BTC-BRL/{self.current_value.get()}")
        xData_bitcoin = []
        yData_bitcoin = []
        yData2_bitcoin = []
        yData3_bitcoin = []
        yData4_bitcoin = []
        
        for x in cotacoes_bitcoin.json():
            ts = int(x['timestamp'])
            xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData_bitcoin.insert(0, xEixo)
            yData_bitcoin.insert(0, float(x['bid']))
            yData2_bitcoin.insert(0, float(x['ask']))
            yData3_bitcoin.insert(0, float(x['low']))
            yData4_bitcoin.insert(0, float(x['high']))
            
    
            self.chart.clear()
            self.chart.plot(xData_bitcoin, yData_bitcoin, marker = 'o', label='compra')
            self.chart.plot(xData_bitcoin, yData2_bitcoin, marker = 'o', label='venda')
            self.chart.plot(xData_bitcoin, yData3_bitcoin, marker = 'o', label='mínimo')
            self.chart.plot(xData_bitcoin, yData4_bitcoin, marker = 'o', label='máximo')
            self.chart.set_title("Bitcon")
            self.chart.set_xlabel('Quantidade de Dias')
            self.chart.set_ylabel('BRL')
            self.chart.grid()
            self.chart.legend()
            self.figure_canvas.draw()
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()