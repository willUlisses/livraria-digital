from config.connection import criar_conexao

def inserir_autor(nome: str, nacionalidade: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO autores (nome, nacionalidade, ativo) VALUES (%s, %s, TRUE)"
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
        sql = "UPDATE autores SET ativo = FALSE WHERE id_autor = %s"
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
        sql = "SELECT a.nome FROM autores a WHERE nome ILIKE %s AND a.ativo = TRUE"
        cursor.execute(sql, (nome_busca,))
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Não foi possível buscar por autor: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_todos_autores():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT id_autor, nome FROM autores WHERE ativo = TRUE"
        cursor.execute(sql)
        autores = cursor.fetchall()
        return autores
    except Exception as e:
        print(f"Erro ao listar autores do sistema: {e}") 
    finally:
        cursor.close()
        conn.close()

def modificar_nome_autor(nome: str, id_autor: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "UPDATE autores SET nome = %s WHERE id_autor = %s"
        cursor.execute(sql, (nome, id_autor))
        conn.commit()
    except Exception as e:
        print(f"Erro ao modificar nome do autor: {e}")
    finally:
        cursor.close()
        conn.close()

def tem_autor(id_autor: int) -> bool:
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT id_autor FROM autores WHERE id_autor = %s AND ativo = TRUE"
        cursor.execute(sql, (id_autor,))
        autor = cursor.fetchone()
        if autor:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao encontrar autor: {e}")
    finally:
        cursor.close()
        conn.close()

