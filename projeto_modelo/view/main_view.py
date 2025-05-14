# view/main_view.py
# Formulário Principal da aplicação com menu de navegação

import customtkinter as ctk
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
        self.title("Sistema de Gerenciamento de Alunos")
        self.geometry("800x600")
        self.configurar_menu()

    def configurar_menu(self):
        # Menu principal
        menu_bar = ctk.CTkMenu(self)

        # Menu Arquivo
        menu_arquivo = ctk.CTkMenu(menu_bar, tearoff=0)
        menu_arquivo.add_command(label="Abrir Grid Alunos", command=self.abrir_grid_alunos)
        menu_arquivo.add_command(label="Abrir Form Aluno", command=self.abrir_form_alunos)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.destroy)

        # Menu Gráficos
        menu_graficos = ctk.CTkMenu(menu_bar, tearoff=0)
        menu_graficos.add_command(label="Idade dos Alunos", command=self.abrir_grafico_idade)
        menu_graficos.add_command(label="Quantidade de Alunos", command=self.abrir_grafico_quantidade)

        # Menu Relatórios
        menu_relatorios = ctk.CTkMenu(menu_bar, tearoff=0)
        menu_relatorios.add_command(label="Impressão do Form Alunos", command=self.abrir_relatorio)

        # Menu Sobre
        menu_sobre = ctk.CTkMenu(menu_bar, tearoff=0)
        menu_sobre.add_command(label="Sobre", command=self.abrir_sobre)
        menu_sobre.add_command(label="Licença", command=self.abrir_licenca)

        # Adicionar menus à barra
        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_bar.add_cascade(label="Gráficos", menu=menu_graficos)
        menu_bar.add_cascade(label="Relatórios", menu=menu_relatorios)
        menu_bar.add_cascade(label="Sobre", menu=menu_sobre)

        # Configurar a janela para usar a barra de menu
        self.config(menu=menu_bar)

    # Funções de navegação
    def abrir_grid_alunos(self):
        GridAlunos(self)

    def abrir_form_alunos(self):
        FormAlunos(self)

    def abrir_grafico_idade(self):
        FormIdadeAlunos(self)

    def abrir_grafico_quantidade(self):
        FormQuantidadeAlunos(self)

    def abrir_relatorio(self):
        ReportAlunos(self)

    def abrir_sobre(self):
        FormSobre(self)

    def abrir_licenca(self):
        FormLicenca(self)

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
