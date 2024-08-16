import customtkinter as ctk # importanto a biblioteca >> install



janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)


btn1 = ctk.CTkButton(janela, text="BOTÃO 1")
btn1.place(x=20, y=0)
btn2 = ctk.CTkButton(janela, text="BOTÃO 2").place(x=20, y=40)

#posicionando com responsividade
btn3 = ctk.CTkButton(janela, text="BOTÃO 3").place(relx=0.1, rely=0.2)








janela.mainloop()