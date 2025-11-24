import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname="livraria",
            user="postgres",
            password="1nvalidDB",
            host="localhost",
            port="5432"
        )
        #print("Conexão Realizada com sucesso")
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco: {e}")
        return None