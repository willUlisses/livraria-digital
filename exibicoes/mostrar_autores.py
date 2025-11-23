import time

def mostrar_todos_autores(autores):
    for autor in autores:
        time.sleep(0.7)
        print("------------------")
        print(f"ID: {autor[0]} - Nome: {autor[1]}")
        print("------------------")

def mostrar_autores_buscados(autores):
    pass