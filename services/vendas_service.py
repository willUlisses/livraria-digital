from config.connection import criar_conexao

def inserir_venda(id_cliente: int, data_venda: str, valor_total: int) -> int:
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO vendas(id_cliente, data_venda, valor_total) values (%s, %s, %s) RETURNING id_venda"
        cursor.execute(sql, (id_cliente, data_venda, valor_total))
        id_venda_feita = cursor.fetchone()[0] #index 0 para retornar apenas o que precisamos: o id da venda feita
        conn.commit()
        return id_venda_feita
    except Exception as e:
        print(f"Erro ao cadastrar nova venda: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def listar_vendas():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT v.id_venda, c.email, v.data_venda, v.valor_total FROM vendas v JOIN clientes c ON v.id_cliente = c.id_cliente"
        cursor.execute(sql)
        vendas = cursor.fetchall()
        return vendas
    except Exception as e:
        print(f"Erro ao cadastrar nova venda: {e}")
    finally:
        cursor.close()
        conn.close()

def cadastrar_item_venda(id_venda: int, id_livro: int, quantidade: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO itens_venda(id_venda, id_livro, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id_venda, id_livro, quantidade))
        conn.commit()
    except Exception as e:
        print(f"Erro ao cadastrar item na venda: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def remover_venda_por_id(id_venda: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM vendas WHERE id_venda = %s"
        cursor.execute(sql, (id_venda,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar venda: {e}")
    finally:
        cursor.close()
        conn.close()

def possui_venda(id_venda: int) -> bool:
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT id_venda FROM vendas WHERE id_venda = %s"
        cursor.execute(sql, (id_venda,))
        venda = cursor.fetchone()
        if venda:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao procurar por venda: {e}")
    finally:
        cursor.close()
        conn.close()