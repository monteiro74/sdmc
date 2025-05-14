# view/form_quantidade_alunos.py
# Gráfico de Quantidade de Alunos

import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from controller.aluno_controller import contar_alunos

class FormQuantidadeAlunos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gráfico de Quantidade de Alunos")
        self.geometry("500x400")

        # Busca os dados
        total_alunos = contar_alunos()

        # Plotar o gráfico
        fig, ax = plt.subplots()
        ax.bar(["Alunos"], [total_alunos], color='green')
        ax.set_title("Quantidade Total de Alunos")
        ax.set_ylabel("Total")

        # Inserir no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()
