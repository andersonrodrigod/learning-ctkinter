import customtkinter as ctk # importanto a biblioteca >> install
from tkinter import *
from PIL import Image


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)

switch_var = ctk.StringVar(value="on")

def event():
    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("Light")
    elif switch_var.get() == "Desativado":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("System")
    pass

switch = ctk.CTkSwitch(janela, 
                       text=None,
                       command=event,
                       variable=switch_var,
                       onvalue="Ativado",
                       offvalue="Desativado")


switch.pack(pady=30)




janela.mainloop()
