import tkinter as tk
from tkinter import StringVar, Frame, Label, LEFT, RAISED, NW, Entry, Button
from tkinter import ttk

# Importando Pillow
from PIL import Image, ImageTk

# Importando TKcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

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
janela.title('Tkinter')
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

# Trabalhando no frame cima



# Abrindo imagem

app_img = Image.open('inventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventário Doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Trabalhando no frame meio

# Criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief='solid')
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text='Sala/Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief='solid')
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief='solid')
e_descricao.place(x=130, y=71)

l_modelo = Label(frameMeio, text='Marca/Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMeio, width=30, justify='left', relief='solid')
e_modelo.place(x=130, y=101)

l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12,background='black', bordewidth=2, year=2024)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief='solid')
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text='Número de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief='solid')
e_serial.place(x=130, y=191)

# Criando botões ---------------------------

# Botão carregar
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, width=29, text='carregar'.upper(), height=1,compound='center', anchor='center',overrelief='ridge', font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=220)

# Botão inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, image=img_add, width=95, text='  Adicionar'.upper(), compound='left', anchor=NW, overrelief='ridge', font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

# Botão atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, image=img_update, width=95, text='  Atualizar'.upper(), compound='left', anchor=NW, overrelief='ridge', font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

# Botão deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, image=img_delete, width=95, text='  Deletar'.upper(), compound='left', anchor=NW, overrelief='ridge', font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

# Botão ver imagem
img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, image=img_item, width=95, text='  Ver item'.upper(), compound='left', anchor=NW, overrelief='ridge', font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=221)

# Labels quantidade total e valores

l_total = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_total.place(x=10, y=70)


janela.mainloop()
