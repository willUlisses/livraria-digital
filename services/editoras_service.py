from config.connection import criar_conexao

def inserir_editora(nome: str, cidade: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO editoras(nome, cidade, ativo) VALUES (%s, %s, TRUE)"
        cursor.execute(sql, (nome, cidade))
        conn.commit()
        print(f"\nEditora {nome} inserida com sucesso no banco!")
    except Exception as e:
        print(f"\nErro ao inserir nova editora: {e}")
    finally:
        cursor.close()
        conn.close()

def remover_editora_por_id(id_editora: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "UPDATE editoras SET ativo = FALSE WHERE id_editora = %s"
        cursor.execute(sql, (id_editora,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao remover editora: {e}")
    finally:
        cursor.close()
        conn.close()

    
def alterar_nome_editora(nome: str, id_editora: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "UPDATE editoras SET nome = %s WHERE id_editora = %s"
        cursor.execute(sql, (nome, id_editora))
        conn.commit()
        print(f"\nNome da editora alterado para: {nome}")
    except Exception as e:
        print(f"Erro ao alterar editora: {e}")
    finally:
        cursor.close()
        conn.close()


def listar_editoras():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT id_editora, nome FROM editoras WHERE ativo = TRUE"
        cursor.execute(sql)
        editoras = cursor.fetchall()
        return editoras
    except Exception as e:
        print(f"\nErro ao listar editoras: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_editora_por_nome(nome_editora: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        nome_de_busca = f"%{nome_editora}%"
        sql = "SELECT nome, cidade FROM editoras WHERE nome ILIKE %s AND ativo = TRUE"
        cursor.execute(sql, (nome_de_busca,))
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
         print(f"Erro ao buscar por editoras: {e}")
    finally:
        cursor.close()
        conn.close()  

def possui_editora(id_editora: int) -> bool:
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT id_editora FROM editoras WHERE id_editora = %s AND ativo = TRUE"
        cursor.execute(sql, (id_editora,))
        editora = cursor.fetchone()
        if editora:
            return True
        else: 
            return False
    except Exception as e:
        print(f"Erro ao procurar por editora: {e}")
    finally:
        cursor.close()
        conn.close() 

