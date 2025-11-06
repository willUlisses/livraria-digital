from config.connection import criar_conexao

#Registrar novo Cliente
def registrar(telefone: str, email: str, senha: str):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        sql = "ISNERT INTO clientes (telefone, senha, email) VALUES (%s, %s, %s)"
    except Exception as e:
        print(f"Erro ao registrar-se: {e}")

#Logar em um cliente
def login(email: str, senha: str):
    pass