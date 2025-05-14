# model/conexao_db.py
# Conexão com o MySQL lendo as configurações do arquivo conexao.con

import mysql.connector

def ler_conexao(arquivo='conexao.con'):
    """Lê as configurações de conexão do arquivo .con"""
    config = {}
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            if '=' in linha:
                chave, valor = linha.strip().strip(';').split('=')
                config[chave.strip()] = valor.strip().strip("'")
    return config

def obter_conexao():
    """Estabelece a conexão com o banco de dados"""
    config = ler_conexao()
    try:
        conn = mysql.connector.connect(
            host=config['server'],
            port=config['port'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Erro de conexão: {e}")
        raise
