import tkinter as tk
from tkinter import StringVar
from tkinter import ttk

# Cores
co0 = "#2e2d2b"  # preto
co1 = "#feffff"  # branco
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# Criando janela
janela = tk.Tk()
janela.title('Exemplo de tkinter')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

janela.mainloop()
