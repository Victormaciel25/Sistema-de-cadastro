import tkinter as tk
from tkinter import StringVar, Frame
from tkinter import ttk

from PIL import Image, ImageTk

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

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=tk.FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=tk.FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=tk.NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=tk.FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=tk.NSEW)

# Abrindo imagem



janela.mainloop()
