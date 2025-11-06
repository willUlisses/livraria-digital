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
        sql = f"DELETE FROM livros WHERE id_livro = {id_livro}"
        cursor.execute(sql, (id_livro))
        conn.commit()
        print("Livro removido com sucesso!")
    except Exception as e:
        print(f"Erro ao remover livro: {e}")
    finally:
        cursor.close()
        conn.close()

## --------------------------------------------- alterar algo em um livro
def alterar_livro(id_livro: int): # apenas para ADMIN
    pass

## ------------------------------------------------ listar livros do user logado
def listar_livros(): # tanto pra USER quanto Pra ADMIN
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "..." 
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
    finally:
        cursor.close()
        conn.close()