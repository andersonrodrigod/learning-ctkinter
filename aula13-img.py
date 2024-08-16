import customtkinter as ctk # importanto a biblioteca >> install
from tkinter import *
from PIL import Image


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela


ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20)

img1 = ctk.CTkImage(light_image=Image.open("./youtube.jpg"), dark_image=Image.open("./youtube.jpg"), size=(80, 80))

ctk.CTkLabel(janela, text=None, image=img1).pack()







'''

img = ctk.CTkImage(light_image=Image.open("./youtube.jpg"), dark_image=Image.open("./youtube.jpg"), size=(80, 80))
def evento():
    print("Ja foi para o youtube")
    pass


ctk.CTkButton(janela,
              text="Youtube",
              command=evento,
              width=300,
              height=100,
              fg_color="transparent",
              hover_color="green",
              text_color="red",
              font=("arial bold", 16),
              border_color="#fff",
              border_width=3,
              border_spacing=20, 
              corner_radius=20,
              state="normal",
              image=img).pack(pady=30)

'''
janela.mainloop()