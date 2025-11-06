from config.connection import criar_conexao
conn = criar_conexao()
if conn:
    print("Conexão bem-sucedida!")
else:
    print("Falha na conexão.")