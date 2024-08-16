import customtkinter as ctk # importanto a biblioteca >> install


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela


ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20)



# Trabalhando com label de forma dinamica
#1 Forma introduzeindo texto por input

'''ctk.CTkLabel(janela, text="Digite seu nome completo").pack()

text_var = ctk.StringVar(value=input("Olá mundo! este texto é dinâmico"))
lab = ctk.CTkLabel(janela,
                   textvariable=text_var,
                   width=200,
                   height=25,
                   text_color="red",
                   font=("arial bold", 16))

lab.pack(pady=10)

'''


#2 Introduzindo texto por entry (forma mais pratica)

ctk.CTkLabel(janela, text="Digite seu nome completo").pack()

def enviar():
    t = entry.get()
    lab.configure(text=str(t))
    pass
    

text_var = ctk.StringVar(value="Olá mundo! este texto é dinâmico")
lab = ctk.CTkLabel(janela,
                   text="",
                   width=200,
                   height=25,
                   text_color="red",
                   font=("arial bold", 16),
                         fg_color="teal",
                         corner_radius=10,)

lab.pack(pady=10)

entry = ctk.CTkEntry(janela, width=200)
entry.pack()

ctk.CTkButton(janela, text="Enviar", width=200, command=enviar).pack(pady=10)


janela.mainloop()