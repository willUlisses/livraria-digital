from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *
import os
import sys
import time

user_logged = None

while True:
    login_user_panel()
    try:
        login_option = int(input("Informe o que quer fazer: "))
    except ValueError:
        print("Você pode informar as opções apenas com números.")
    if login_option == 1:
        os.system("cls")
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
        os.system("cls")
        print("Informe seus dados\n")
        email = input("Email: ")
        senha = pwinput("Senha: ")
        user_logged = login(email, senha)
        os.system("cls")
        break
    elif login_option == 3:
        print("Encerrando o sistema...")
        time.sleep(3)
        sys.exit(0)
        break
    else:
        print("Opção inválida, tente novamente.")
        continue

while True:
    if user_logged[0] == 1: ##para o caso de ser admin
        admin_option_panel()
    else: #para o caso de ser um usuário normal
        user_options_panel()
        

