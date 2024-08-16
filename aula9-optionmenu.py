import customtkinter as ctk # importanto a biblioteca >> install


janela = ctk.CTk() # Cria a janela

# Configurando a janela principal
janela.title("App Teste") #titulo do app
janela.geometry("700x400") # tamanho da tela


ctk.CTkLabel(janela, text="Menu de opções", font=("arial bold", 20)).pack(pady=20)

ctk.CTkLabel(janela, text="Escolha o seu mês de nascimento", font=("aial bold", 14)).pack()

mes_var = ctk.StringVar(value="Escolha o mês")

def mes_nascimento(escolha):
    print(f"O seu mês de nascimento é: {escolha}")

mes = ctk.CTkOptionMenu(janela, 
                        values= ["Janeiro", "Feveireio", "Março", "Abril", "Maio", "Junho", "Outros..."], command=mes_nascimento, 
                        variable=mes_var,
                        width=250,
                        height=50,
                        corner_radius=50,
                        fg_color="red",
                        button_color="green",
                        button_hover_color="teal",
                        dropdown_fg_color="teal",
                        dropdown_text_color="red",
                        dropdown_font=("arial bold", 15),
                        dropdown_hover_color="white"


                )
mes.pack(pady=10)
mes.set("Escolha o mês")

'''mes = ctk.CTkOptionMenu(janela, 
                        values= ["Janeiro", "Feveireio", "Março", "Abril", "Maio", "Junho", "Outros..."], command=mes_nascimento
                )
mes.pack(pady=10)
mes.set("Escolha o mês")'''






janela.mainloop()