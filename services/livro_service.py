from config.connection import criar_conexao

## inserir um livro na tabela
def inserir_livro(titulo, data_lancamento, id_editora):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO livros (titulo, data_lancamento, id_editora) VALUES (%s, %s)"
        cursor.execute(sql, (titulo, data_lancamento, id_editora)) #necessário adicionar verificação da existência da editora
        conn.commit()
        print("Livro adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir livro: {e}")
    finally:
        cursor.close()
        conn.close()

## retirar um livro da tabela pelo id
def remover_livro(id_livro):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM livros WHERE id_livro = %s"
        cursor.execute(sql, (id_livro))
        conn.commit()
        print("Livro removido com sucesso!")
    except Exception as e:
        print(f"Erro ao remover livro: {e}")
    finally:
        cursor.close()
        conn.close()

## alterar algo em um livro
def alterar_livro(id_livro):
    pass

## listar livros do user logado
def listar_livros():
    pass