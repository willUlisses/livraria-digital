from config.connection import criar_conexao

def inserir_editora(nome: str, cidade: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO editoras(nome, cidade) VALUES (%s, %s)"
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
        sql = f"DELETE FROM editoras WHERE id_editora = {id_editora}"
        cursor.execute(sql, (id_editora))
        conn.commit()
        print("\nEditora removida do banco com sucesso!")
    except Exception as e:
        print(f"Erro ao remover editora: {e}")
    finally:
        cursor.close()
        conn.close()

    
def alterar_nome_editora(nome, id_editora):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "ALTER TABLE editoras SET nome = %s WHERE id_editora = %s"
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
        sql = "SELECT id_editora, nome FROM editoras"
        cursor.execute(sql)
        editoras = cursor.fetchall()
        return editoras
    except Exception as e:
        print(f"\nErro ao listar editoras: {e}")
    finally:
        cursor.close()
        conn.close()

