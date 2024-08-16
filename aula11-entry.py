import customtkinter as ctk # importanto a biblioteca >> install
from tkinter import *

janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela


ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20)

entry = ctk.CTkEntry(janela, 
                    width=300,
                    placeholder_text="Digite seu nome completo",
                    placeholder_text_color="green",
                    fg_color="transparent",
                    text_color="teal",
                    font=("arial bold", 16),
                    border_width=10,
                    border_color="#fff",
                    state="normal",
                    corner_radius=20)

entry.pack(pady=20)

def pegar():
    print(entry.get())
    entry.delete(0, END)
    pass

'''def apagar():
    pass
'''

ctk.CTkButton(janela, width=300, text="Pegar texto", command=pegar).pack()


'''ctk.CTkButton(janela, width=300, text="Apagar texto", command=apagar).pack(pady=5)'''


janela.mainloop()