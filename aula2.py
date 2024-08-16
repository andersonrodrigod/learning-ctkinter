import customtkinter as ctk # importanto a biblioteca >> install

janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela
janela.maxsize(width=900, height=550) # maximo da tela
janela.minsize(width=500, height=300) # minimo da tela
janela.resizable(width=False, height=False) # desativa opção de maximizar
'''janela.iconify()'''  #fecha app
'''janela.deiconify()''' # abre app nao ta funcionando


janela.mainloop()