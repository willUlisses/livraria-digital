from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *

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
        ja_existe = valida_registro(email)
        if ja_existe:
            print(f"\nO email {email} já está cadastrado\n")
            break
    elif login_option == 2:
        pass
    elif login_option == 3:
        break
    else:
        print("Opção inválida, tente novamente.")
        continue