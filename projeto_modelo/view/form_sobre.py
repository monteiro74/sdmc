# view/form_sobre.py
# Tela de informações "Sobre o Sistema"

import customtkinter as ctk

class FormSobre(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Sobre o Sistema")
        self.geometry("500x400")
        
        ctk.CTkLabel(self, text="Sistema de Gerenciamento de Alunos", font=("Arial", 18)).pack(pady=20)
        ctk.CTkLabel(self, text="""Desenvolvido para facilitar o controle de alunos.
                                 Interface moderna em CustomTkinter.
                                 Conexão com banco de dados MySQL.
                                 CRUD completo, gráficos e relatórios.""",
                                 font=("Arial", 12)).pack(pady=10)

        ctk.CTkButton(self, text="Fechar", command=self.destroy).pack(pady=20)
