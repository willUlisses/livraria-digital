from config.connection import criar_conexao
from psycopg2.errors import ForeignKeyViolation
from psycopg2.errors import IntegrityError

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
        sql = "DELETE FROM editoras WHERE id_editora = %s"
        cursor.execute(sql, (id_editora,))
        conn.commit()
        print("\nEditora removida do banco com sucesso!")
    except ForeignKeyViolation:
        raise ForeignKeyViolation
    except IntegrityError:
        print("erro de integridade")
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

def buscasr_editora_por_nome(nome_editora: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        nome_de_busca = f"%{nome_editora}%"
        sql = "SELECT nome, cidade FROM editoras WHERE nome ILIKE %s"
        cursor.execute(sql, (nome_de_busca,))
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
         print(f"Erro ao buscar por editoras: {e}")
    finally:
        cursor.close()
        conn.close()   

