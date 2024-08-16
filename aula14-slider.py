import customtkinter as ctk # importanto a biblioteca >> install
from tkinter import *
from PIL import Image


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)

def slider_value(value):
    if value == 10:
        slider.configure(fg_color="red")
    else:
        slider.configure(fg_color="blue")
    print(value)

slider = ctk.CTkSlider(janela, from_=10, to=100, command=slider_value, width=500)
slider.pack(pady=30)

janela.mainloop()