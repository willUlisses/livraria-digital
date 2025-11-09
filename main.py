from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *
import os
import time

user_logged = None

while True:
    login_user_panel()
    try:
        login_option = int(input("Informe o que quer fazer: "))
    except ValueError:
        print("Você pode informar as opções apenas com números.")
    if login_option == 1:
        print("Informe seus dados\n")
        email = input("Email: ")
        senha = pwinput("Senha: ")
        telefone = input("Telefone: ")
        ja_existe = valida_registro(email)
        if ja_existe:
            print(f"\nO email {email} já está cadastrado\n")
            continue
        registrar(email, senha, telefone)
        os.system("cls")
        print("Agora faça o login com suas credenciais")
        time.sleep(3)
        os.system("cls")
    elif login_option == 2:
        print("Informe seus dados\n")
        email = input("Email: ")
        senha = pwinput("Senha: ")
        user_logged = login(email, senha)
        break
    elif login_option == 3:
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")
        continue

