# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:08:16 2025

@author: usuario
"""

import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("light")  # Modo claro (ou "dark")
ctk.set_default_color_theme("blue")  # Tema azul

# Criação da janela principal
app = ctk.CTk()  
app.title("Hello World com CustomTkinter")
app.geometry("400x200")

# Label (Texto)
label = ctk.CTkLabel(app, text="Hello, World!", font=("Arial", 24))
label.pack(pady=20)

# Botão para fechar a janela
botao = ctk.CTkButton(app, text="Fechar", command=app.destroy)
botao.pack(pady=10)

# Inicia o loop da aplicação
app.mainloop()
