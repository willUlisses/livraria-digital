from config.connection import criar_conexao

def inserir_autor(nome: str, nacionalidade: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO autores (nome, nacionalidade) VALUES (%s, %s)"
        cursor.execute(sql, (nome, nacionalidade))
        conn.commit()
        print(f"\nO autor {nome} foi inserido com sucesso no banco!")
    except Exception as e:
        print(f"Erro ao inserir novo autor: {e}")
    finally:
        cursor.close()
        conn.close()

def remover_autor_por_id(id_autor: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM autores WHERE id_autor = %s"
        cursor.execute(sql, (id_autor,))
        conn.commit()
        print("\nAutor removido do banco com sucesso!")
    except Exception as e:
        print(f"\nErro ao remover autor: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_autor_por_nome(nome_autor: str) -> str:
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        nome_busca = f"%{nome_autor}%"
        sql = "SELECT a.nome FROM autores a WHERE nome ILIKE %s"
        cursor.execute(sql, (nome_busca,))
        resultados = cursor.fetchone()
        return resultados
    except Exception as e:
        print(f"Não foi possível buscar por autor: {e}")
    finally:
        cursor.close()
        conn.close() 
