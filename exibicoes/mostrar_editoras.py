import time

def mostrar_editoras(editoras_existentes):
    for editora in editoras_existentes:
        time.sleep(0.7)
        print("------------------")
        print(f"ID: {editora[0]}\nNome: {editora[1]}")
        print("------------------")