import customtkinter as ctk # importanto a biblioteca >> install


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela
janela.maxsize(width=900, height=550) # maximo da tela
janela.minsize(width=500, height=300) # minimo da tela
janela.resizable(width=False, height=False) # desativa opção de maximizar


# Tabview
tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=5, border_color="red", fg_color="teal", segmented_button_fg_color="red", segmented_button_selected_color="green", segmented_button_selected_hover_color="blue", segmented_button_unselected_hover_color="yellow")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)


# Adicionando elementos na nossa tab

text = ctk.CTkLabel(tabview.tab("Nomes"), text="Rodrigo Rodrigues\nJefferson Rodrigues\nRobson Rodrigues")
text.pack()
idd = ctk.CTkLabel(tabview.tab("Idades"), text="29\n32\n27")
idd.pack()
idd = ctk.CTkLabel(tabview.tab("Genero"), text="Masculino\nMasculino\nMasculino")
idd.pack()


janela.mainloop()