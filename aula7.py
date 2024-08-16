import customtkinter as ctk # importanto a biblioteca >> install


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela
janela.maxsize(width=900, height=550) # maximo da tela
janela.minsize(width=500, height=300) # minimo da tela
janela.resizable(width=False, height=False) # desativa opção de maximizar


# TextBox (Caixa de texto no Customtkinter)

textbox = ctk.CTkTextbox(janela, width=300, height=350, scrollbar_button_color="green", scrollbar_button_hover_color="red", border_color="red", border_width=2, corner_radius=15, fg_color="teal", border_spacing=20, activate_scrollbars=True)
textbox.pack()

textbox.insert("0.0", "Título do seu texto" + "Olá dev, estou aqui progrmando interfaces graficas com custom no cana, set-escola de programação e está sendo uma boa. \n\n"*20)


janela.mainloop()