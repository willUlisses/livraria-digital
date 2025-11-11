from config.connection import criar_conexao

def inserir_venda(id_cliente: int, data_venda: str, valor_total: int):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO vendas(id_cliente, data_venda, valor_total) values (%s, %s, %s)"
        cursor.execute(sql, (id_cliente, data_venda, valor_total))
        conn.commit()
        print("\nVenda cadastrada com sucesso")
    except Exception as e:
        print(f"Erro ao cadastrar nova venda: {e}")
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