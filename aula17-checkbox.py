import customtkinter as ctk # importanto a biblioteca >> install



janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)

check_var = ctk.StringVar(value="on")

def check_value():
    valor = check_var.get()
    if valor == "on":
        print("Tema Claro")
    elif valor == "off":
        print("Tema escuro")
    else:
        print("Tema do sistema")
    print(valor)

checkbox = ctk.CTkCheckBox(janela, text="Altere o tema", variable=check_var, onvalue="on", offvalue="off", command=check_value )

checkbox.pack(pady=10)

janela.mainloop()