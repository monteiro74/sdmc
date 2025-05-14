# controller/aluno_controller.py
# Operações CRUD para Alunos

from model.conexao_db import obter_conexao

def obter_alunos():
    """Retorna a lista de alunos cadastrados."""
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT matricula, nome, curso, idade FROM alunos")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return alunos

def obter_aluno_por_matricula(matricula):
    """Retorna os dados de um aluno específico."""
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alunos WHERE matricula = %s", (matricula,))
    aluno = cursor.fetchone()
    cursor.close()
    conn.close()
    return aluno

def salvar_aluno(dados):
    """Insere ou atualiza um aluno no banco."""
    conn = obter_conexao()
    cursor = conn.cursor()
    if dados.get("matricula"):
        # Atualiza se a matrícula já existe
        cursor.execute("""
            UPDATE alunos SET nome=%s, curso=%s, idade=%s, foto=%s WHERE matricula=%s
        """, (dados["nome"], dados["curso"], dados["idade"], dados["foto"], dados["matricula"]))
    else:
        # Insere um novo aluno
        cursor.execute("""
            INSERT INTO alunos (matricula, nome, curso, idade, foto) VALUES (%s, %s, %s, %s, %s)
        """, (dados["matricula"], dados["nome"], dados["curso"], dados["idade"], dados["foto"]))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_aluno(matricula):
    """Remove um aluno do banco."""
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE matricula = %s", (matricula,))
    conn.commit()
    cursor.close()
    conn.close()

def contar_alunos():
    """Conta o total de alunos cadastrados."""
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM alunos")
    total = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total

def obter_idades_alunos():
    """Retorna as idades dos alunos para análise de gráficos."""
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT idade FROM alunos")
    idades = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return idades
