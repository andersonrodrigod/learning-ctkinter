import customtkinter as ctk # importanto a biblioteca >> install
from tkinter import *
from PIL import Image


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)

def btn(value):
    print("está no segmento de: ", value)
    pass

segment = ctk.CTkSegmentedButton(janela,
                                 values=["Tkinter", "Django", "flesk"],
                                command=btn )


segment.pack(pady=20)
segment.set("Tkinter")




janela.mainloop()




