# controller/relatorio_controller.py
# Controlador para geração de relatórios PDF

from model.conexao_db import obter_conexao

def obter_dados_relatorio():
    """Coleta os dados de alunos para o relatório."""
    conn = obter_conexao()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT matricula, nome, curso, idade FROM alunos")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return alunos
