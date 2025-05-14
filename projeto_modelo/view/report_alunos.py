# view/report_alunos.py
# Geração de relatório em PDF com a lista de alunos

import customtkinter as ctk
from fpdf import FPDF
from tkinter import messagebox
from controller.aluno_controller import obter_alunos

class ReportAlunos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Relatório de Alunos")
        self.geometry("400x200")

        ctk.CTkLabel(self, text="Gerar Relatório de Alunos", font=("Arial", 16)).pack(pady=20)
        ctk.CTkButton(self, text="Gerar PDF", command=self.gerar_pdf).pack(pady=10)
        ctk.CTkButton(self, text="Fechar", command=self.destroy).pack(pady=10)

    def gerar_pdf(self):
        alunos = obter_alunos()
        if not alunos:
            messagebox.showinfo("Informação", "Não há alunos cadastrados para gerar o relatório.")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório de Alunos", ln=True, align="C")
        pdf.ln(10)

        # Cabeçalhos
        pdf.cell(40, 10, "Matrícula", border=1)
        pdf.cell(60, 10, "Nome", border=1)
        pdf.cell(40, 10, "Curso", border=1)
        pdf.cell(20, 10, "Idade", border=1)
        pdf.ln()

        # Dados dos alunos
        for aluno in alunos:
            pdf.cell(40, 10, aluno["matricula"], border=1)
            pdf.cell(60, 10, aluno["nome"], border=1)
            pdf.cell(40, 10, aluno["curso"], border=1)
            pdf.cell(20, 10, str(aluno["idade"]), border=1)
            pdf.ln()

        # Salvar o arquivo PDF
        pdf.output("relatorio_alunos.pdf")
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")
