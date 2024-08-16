import customtkinter as ctk # importanto a biblioteca >> install


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela
janela.maxsize(width=900, height=550) # maximo da tela
janela.minsize(width=500, height=300) # minimo da tela
janela.resizable(width=False, height=False) # desativa opção de maximizar


# Frames

frame1 = ctk.CTkFrame(master=janela, width=200, height=330, fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30)
frame1.place(x=10, y=60)
frame2 = ctk.CTkFrame(janela, width=200, height=330, fg_color="green")
frame2.place(x=230, y=60)
frame3 = ctk.CTkFrame(janela, width=200, height=330, fg_color="white")
frame3.place(x=450, y=60)


janela.mainloop()