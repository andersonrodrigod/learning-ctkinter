import customtkinter as ctk # importanto a biblioteca >> install



janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela

ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20, padx=5)

progressbar = ctk.CTkProgressBar(janela)

progressbar.pack(pady=20)
progressbar.start()
#progressbar.step()
progressbar.stop()






janela.mainloop()