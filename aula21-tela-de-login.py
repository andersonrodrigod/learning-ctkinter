import customtkinter as ctk # importanto a biblioteca >> install



janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("Sistema de Login") #titulo do app
janela.geometry("400x500") # tamanho da tela

ctk.CTkLabel(janela, text="Faça Login", font=("arial bold", 20)).pack(pady=10)

ctk.CTkEntry(janela, placeholder_text="Username", width=250, height=45).pack(pady=20)
ctk.CTkEntry(janela, placeholder_text="Senha", width=250, height=45).pack()

ctk.CTkButton(janela, text="Logar".upper(), width=250, height=45).pack(pady=30)





janela.mainloop()