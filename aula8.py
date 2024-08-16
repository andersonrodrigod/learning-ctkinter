import customtkinter as ctk # importanto a biblioteca >> install


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela
janela.maxsize(width=900, height=550) # maximo da tela
janela.minsize(width=500, height=300) # minimo da tela
janela.resizable(width=False, height=False) # desativa opção de maximizar


# Caixa de diálogo

def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de Dialogo", text="Digite o seu número de celular", entry_border_color="red")
    print("Numero de celular buscado", dialog.get_input())

btn = ctk.CTkButton(janela, text="Abrir caixa de diálogo", command=abrir)
btn.pack()


janela.mainloop()