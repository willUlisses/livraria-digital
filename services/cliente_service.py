from config.connection import criar_conexao

#-------------------------------- Registrar novo Cliente
def registrar(email: str, senha: str, telefone: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (email, senha, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (email, senha, telefone))
        conn.commit()
        print(f"Cliente com email: {email} registrado com sucesso")
    except Exception as e:
        print(f"Erro ao registrar-se: {e}")
    finally:
        cursor.close()
        conn.close()

#-------------------------------- Logar em um cliente
def login(email: str, senha: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "SELECT * FROM clientes WHERE email=%s AND senha=%s"
        cursor.execute(sql, (email, senha))
        cliente = cursor.fetchone()
        return cliente
    except Exception as e:
        print(f"Erro ao logar na conta: {e}")
    finally:
        cursor.close()
        conn.close()


def valida_registro(email: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "SELECT email FROM clientes c WHERE email = %s"
        cursor.execute(sql, (email,))
        cliente = cursor.fetchone()
        if cliente:
            return True
        else:
            return False
    except Exception as e:
        print(f"Não foi possível conectar-se ao banco: {e}")
    finally:
        cursor.close()
        conn.close()