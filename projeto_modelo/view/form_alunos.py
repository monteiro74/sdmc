# view/form_alunos.py
# Formulário para cadastro e edição de aluno

import customtkinter as ctk
from tkinter import filedialog, messagebox
from controller.aluno_controller import salvar_aluno, obter_aluno_por_matricula

class FormAlunos(ctk.CTkToplevel):
    def __init__(self, master=None, matricula=None, atualizar_callback=None):
        super().__init__(master)
        self.title("Cadastro de Aluno")
        self.geometry("400x500")
        self.matricula = matricula
        self.atualizar_callback = atualizar_callback
        self.foto_bytes = None

        # Campos
        self.entry_matricula = ctk.CTkEntry(self, placeholder_text="Matrícula")
        self.entry_matricula.pack(pady=10)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.entry_nome.pack(pady=10)
        self.entry_curso = ctk.CTkEntry(self, placeholder_text="Curso")
        self.entry_curso.pack(pady=10)
        self.entry_idade = ctk.CTkEntry(self, placeholder_text="Idade")
        self.entry_idade.pack(pady=10)

        # Botão de foto
        self.botao_foto = ctk.CTkButton(self, text="Selecionar Foto", command=self.selecionar_foto)
        self.botao_foto.pack(pady=5)

        # Botão salvar
        self.botao_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar)
        self.botao_salvar.pack(pady=20)

        if matricula:
            self.carregar_dados()

    def selecionar_foto(self):
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png")])
        if caminho:
            with open(caminho, "rb") as img_file:
                self.foto_bytes = img_file.read()

    def carregar_dados(self):
        aluno = obter_aluno_por_matricula(self.matricula)
        if aluno:
            self.entry_matricula.insert(0, aluno["matricula"])
            self.entry_nome.insert(0, aluno["nome"])
            self.entry_curso.insert(0, aluno["curso"])
            self.entry_idade.insert(0, aluno["idade"])
            self.entry_matricula.configure(state="disabled")
            self.foto_bytes = aluno["foto"]

    def salvar(self):
        dados = {
            "matricula": self.entry_matricula.get(),
            "nome": self.entry_nome.get(),
            "curso": self.entry_curso.get(),
            "idade": self.entry_idade.get(),
            "foto": self.foto_bytes
        }

        if not all([dados["matricula"], dados["nome"], dados["curso"], dados["idade"]]):
            messagebox.showwarning("Validação", "Preencha todos os campos.")
            return

        salvar_aluno(dados)
        if self.atualizar_callback:
            self.atualizar_callback()
        self.destroy()
