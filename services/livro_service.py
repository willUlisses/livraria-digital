from config.connection import criar_conexao

## ------------------------------------------ inserir um livro na tabela
def inserir_livro(titulo: str, data_lancamento: str, id_editora: int): ## apenas para ADMIN
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO livros (titulo, data_lancamento, id_editora) VALUES (%s, %s, %s)"
        cursor.execute(sql, (titulo, data_lancamento, id_editora)) #necessário adicionar verificação da existência da editora
        conn.commit()
        print("Livro adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir livro: {e}")
    finally:
        cursor.close()
        conn.close()

## ------------------------------- retirar um livro da tabela pelo id
def remover_livro_por_id(id_livro: int): # tirar dúvida sobre por ou não por para USER mas para ADMIN com certeza
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM livros WHERE id_livro = %d"
        cursor.execute(sql, (id_livro,))
        conn.commit()
        print("Livro removido com sucesso!")
    except Exception as e:
        print(f"Erro ao remover livro: {e}")
    finally:
        cursor.close()
        conn.close()

## --------------------------------------------- alterar algo em um livro
def alterar__titulo_livro(titulo: str, id_livro: int): # apenas para ADMIN
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "UPDATE livros SET titulo = %s WHERE id_livro = %s"
        cursor.execute(sql, (titulo, id_livro))
        conn.commit()
        print(f"O livro foi alterado com sucesso")
    except Exception as e:
        print(f"Erro ao alterar título do livro: {e}")
    finally:
        cursor.close()
        conn.close()

## ------------------------------------------------ listar livros do user logado
def listar_todos_livros(): # tanto pra USER quanto pra ADMIN
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT l.titulo FROM livros l" 
        cursor.execute(sql)
        conn.commit()
        livros = cursor.fetchall()
        return livros
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_livros_usuario(id_usuario_logado: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT l.titulo FROM clientes c JOIN vendas v on c.id_cliente = v.id_cliente JOIN itens_venda iv on v.id_venda = iv.id_venda JOIN livros l on iv.id_livro = l.id_livro WHERE c.id_cliente = %s"
        cursor.execute(sql, (id_usuario_logado,))
        conn.commit()
        livros_cliente = cursor.fetchall()
        return livros_cliente
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_livro_por_nome(titulo: str) -> str:
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        titulo_busca = f"%{titulo}%"
        sql = "SELECT l.id_livro, l.titulo FROM livros l WHERE l.titulo ILIKE %s"
        cursor.execute(sql, (titulo_busca,))
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Erro ao tentar buscar livro: {e}")
    finally:
        cursor.close()
        conn.close()
