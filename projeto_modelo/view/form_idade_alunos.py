# view/form_idade_alunos.py
# Gráfico de Idade dos Alunos

import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from controller.aluno_controller import obter_idades_alunos

class FormIdadeAlunos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gráfico de Idades dos Alunos")
        self.geometry("600x400")

        # Busca os dados
        idades = obter_idades_alunos()
        faixas = ["18-25", "26-30", "31-40", "41-50", "51+"]
        qtd_idades = [0, 0, 0, 0, 0]

        # Contagem por faixa etária
        for idade in idades:
            if 18 <= idade <= 25:
                qtd_idades[0] += 1
            elif 26 <= idade <= 30:
                qtd_idades[1] += 1
            elif 31 <= idade <= 40:
                qtd_idades[2] += 1
            elif 41 <= idade <= 50:
                qtd_idades[3] += 1
            else:
                qtd_idades[4] += 1

        # Plotar o gráfico
        fig, ax = plt.subplots()
        ax.bar(faixas, qtd_idades, color='blue')
        ax.set_title("Distribuição de Idade dos Alunos")
        ax.set_xlabel("Faixa Etária")
        ax.set_ylabel("Quantidade")

        # Inserir no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()
