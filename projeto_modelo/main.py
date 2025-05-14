# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:08:16 2025

@author: usuario
"""

# view/main_view.py
# Formulário Principal da aplicação com menu de navegação (Modal Ativado)

import customtkinter as ctk
from tkinter import Menu
from view.grid_alunos import GridAlunos
from view.form_alunos import FormAlunos
from view.form_idade_alunos import FormIdadeAlunos
from view.form_quantidade_alunos import FormQuantidadeAlunos
from view.report_alunos import ReportAlunos
from view.form_sobre import FormSobre
from view.form_licenca import FormLicenca

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('light')
        self.title("Sistema de Gerenciamento de Alunos")
        self.geometry("800x600")
        self.configurar_menu()

    def configurar_menu(self):
        # Menu principal usando o tkinter
        menu_bar = Menu(self)

        # Menu Arquivo
        menu_arquivo = Menu(menu_bar, tearoff=0)
        menu_arquivo.add_command(label="Abrir Grid Alunos", command=self.abrir_grid_alunos)
        menu_arquivo.add_command(label="Abrir Form Aluno", command=self.abrir_form_alunos)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.destroy)

        # Menu Gráficos
        menu_graficos = Menu(menu_bar, tearoff=0)
        menu_graficos.add_command(label="Idade dos Alunos", command=self.abrir_grafico_idade)
        menu_graficos.add_command(label="Quantidade de Alunos", command=self.abrir_grafico_quantidade)

        # Menu Relatórios
        menu_relatorios = Menu(menu_bar, tearoff=0)
        menu_relatorios.add_command(label="Impressão do Form Alunos", command=self.abrir_relatorio)

        # Menu Sobre
        menu_sobre = Menu(menu_bar, tearoff=0)
        menu_sobre.add_command(label="Sobre", command=self.abrir_sobre)
        menu_sobre.add_command(label="Licença", command=self.abrir_licenca)

        # Adicionar menus à barra
        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_bar.add_cascade(label="Gráficos", menu=menu_graficos)
        menu_bar.add_cascade(label="Relatórios", menu=menu_relatorios)
        menu_bar.add_cascade(label="Sobre", menu=menu_sobre)

        # Configurar a janela para usar a barra de menu
        self.config(menu=menu_bar)

    # Funções de navegação (Modais)
    def abrir_grid_alunos(self):
        form = GridAlunos(self)
        form.transient(self)  # Modal
        form.grab_set()       # Bloqueia interação no main
        form.focus_set()      # Recebe o foco

    def abrir_form_alunos(self):
        form = FormAlunos(self)
        form.transient(self)
        form.grab_set()
        form.focus_set()

    def abrir_grafico_idade(self):
        form = FormIdadeAlunos(self)
        form.transient(self)
        form.grab_set()
        form.focus_set()

    def abrir_grafico_quantidade(self):
        form = FormQuantidadeAlunos(self)
        form.transient(self)
        form.grab_set()
        form.focus_set()

    def abrir_relatorio(self):
        form = ReportAlunos(self)
        form.transient(self)
        form.grab_set()
        form.focus_set()

    def abrir_sobre(self):
        form = FormSobre(self)
        form.transient(self)
        form.grab_set()
        form.focus_set()

    def abrir_licenca(self):
        form = FormLicenca(self)
        form.transient(self)
        form.grab_set()
        form.focus_set()

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
