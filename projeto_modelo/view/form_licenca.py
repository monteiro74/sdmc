# view/form_licenca.py
# Tela de informações sobre a Licença de Uso

import customtkinter as ctk

class FormLicenca(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Licença de Uso")
        self.geometry("500x400")

        ctk.CTkLabel(self, text="""Este software é de uso acadêmico e educacional.
                     O código é aberto para estudos e melhorias.
                     Proibida a distribuição comercial sem autorização.
                     © 2025 - Sistema de Gerenciamento de Alunos""",
                     font=("Arial", 12)).pack(pady=10)
        ctk.CTkLabel(self, text=texto, font=("Arial", 12)).pack(pady=10)
        ctk.CTkButton(self, text="Fechar", command=self.destroy).pack(pady=20)
