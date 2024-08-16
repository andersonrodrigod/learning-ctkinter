import customtkinter as ctk # importanto a biblioteca >> install


def btn_call():
    print("botão clicado")


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("Sistema de Login") #titulo do app
janela.geometry("400x200") # tamanho da tela
janela.grid_columnconfigure((0, 1), weight=1)


btn = ctk.CTkButton(janela, text="Meu Botão", command=btn_call)
btn.grid(row=0, column=0, pady=20, padx=20, sticky="ew", columnspan=2)


check = ctk.CTkCheckBox(janela, text="CheckBox")
check.grid(row=1, column=0, padx=20, pady=(0,20), sticky="w")

check1 = ctk.CTkCheckBox(janela, text="CheckBox")
check1.grid(row=1, column=1, padx=20, pady=(0,20), sticky="w")







janela.mainloop()



# Testando o git novamente pra verificar no github