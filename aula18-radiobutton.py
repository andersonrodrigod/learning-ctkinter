import customtkinter as ctk # importanto a biblioteca >> install



janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)

radio_var = ctk.IntVar(value=0)

def radio_event(): 
    v = radio_var.get()
    if v == 1:
        print("Masculino")
    else:
        print("Feminino")
    pass

radio1 = ctk.CTkRadioButton(janela, text="Masculino", command=radio_event, variable=radio_var, value=1)
radio2 = ctk.CTkRadioButton(janela, text="Feminino", command=radio_event, variable=radio_var, value=2)

radio1.pack()
radio2.pack()

janela.mainloop()