import time

def mostrar_livros_id_titulo(livros):
    for livro in livros:
        time.sleep(0.7)
        print("------------------")
        print(f"ID:{livro[0]} -> Título: {livro[1]}")
        print("------------------")

def mostrar_livros_titulo(livros):
    for livro in livros:
        time.sleep(0.7)
        print("------------------")
        print(f"Título: {livro[0]}")
        print("------------------")

def mostrar_livros_preco(livros):
    for livro in livros:
        time.sleep(0.7)
        print("------------------")
        print(f"{livro[0]} -> {livro[1]} - R${livro[2]}")
        print("------------------")
                        