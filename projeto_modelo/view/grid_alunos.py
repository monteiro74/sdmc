# view/grid_alunos.py
# Grid de alunos com listagem e botões de CRUD

import customtkinter as ctk
from tkinter import ttk, messagebox
from controller.aluno_controller import obter_alunos, deletar_aluno
from view.form_alunos import FormAlunos

class GridAlunos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Lista de Alunos")
        self.geometry("800x400")

        # Título
        ctk.CTkLabel(self, text="Alunos Cadastrados", font=("Arial", 16)).pack(pady=10)

        # Grid
        self.tree = ttk.Treeview(self, columns=("matricula", "nome", "curso", "idade"), show="headings")
        self.tree.heading("matricula", text="Matrícula")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("curso", text="Curso")
        self.tree.heading("idade", text="Idade")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<Double-1>", self.editar_selecionado)

        # Botões
        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)

        ctk.CTkButton(frame, text="Adicionar", command=self.adicionar).pack(side="left", padx=5)
        ctk.CTkButton(frame, text="Editar", command=self.editar_selecionado).pack(side="left", padx=5)
        ctk.CTkButton(frame, text="Excluir", command=self.excluir).pack(side="left", padx=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for aluno in obter_alunos():
            self.tree.insert("", "end", values=(aluno["matricula"], aluno["nome"], aluno["curso"], aluno["idade"]))

    def adicionar(self):
        FormAlunos(self, atualizar_callback=self.atualizar_lista)

    def editar_selecionado(self, event=None):
        item = self.tree.focus()
        if not item:
            messagebox.showwarning("Seleção", "Selecione um aluno.")
            return
        matricula = self.tree.item(item)["values"][0]
        FormAlunos(self, matricula=matricula, atualizar_callback=self.atualizar_lista)

    def excluir(self):
        item = self.tree.focus()
        if not item:
            messagebox.showwarning("Seleção", "Selecione um aluno.")
            return
        matricula = self.tree.item(item)["values"][0]
        if messagebox.askyesno("Confirmação", f"Deseja excluir o aluno {matricula}?"):
            deletar_aluno(matricula)
            self.atualizar_lista()
