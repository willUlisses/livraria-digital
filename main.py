from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *
from services.livro_service import *
import os
import sys
import time

user_logged = None

while True:
    login_user_panel()
    try:
        login_option = int(input("Informe o que quer fazer: "))
    except ValueError:
        os.system("cls")
        print("Você pode informar as opções apenas com números.")
        continue    

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
        time.sleep(1)
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
        os.system("cls")
        print("Encerrando o sistema...")
        time.sleep(3)
        sys.exit(0)
        break
    else:
        os.system("cls")
        print("Opção inválida, tente novamente.")
        time.sleep(2)
        continue

while True:
    if user_logged[1] == "admin@admin.com": ##para o caso de ser admin
        while True:
            admin_option_panel()
            try:
                admin_option = int(input("\nDigite a opção: "))
            except ValueError:
                os.system("cls")
                print("Você deve digitar apenas números.")
                continue
            if admin_option == 1:
                os.system("cls")
                while True:
                    admin_livros_panel()
                    try:
                        livros_option = int(input("Digite sua opção: "))
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas números.")
                        time.sleep(1)
                        continue

                    #match case
            elif admin_option == 2:
                while True:
                    admin_editoras_panel()
                    try:
                        editoras_option = int(input("Digite sua opção: "))
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas números.")
                        time.sleep(1)
                        continue

                    #match case
            elif admin_option == 3:
                while True:
                    admin_autores_panel()
                    try:
                        autores_option = int(input("Digite sua opção: "))
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas números.")
                        time.sleep(1)
                        continue

                    #match case
            elif admin_option == 4:
                while True:
                    admin_vendas_panel()
                    try:
                        vendas_option = int(input("Digite sua opção: "))
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas números.")
                        time.sleep(1)
                        continue

                    #match case
    else: #para o caso de ser um usuário normal
        while True:
            user_options_panel()
            try:
                user_option = int(input("Informe sua opçao: "))
            except ValueError:
                print("\nInforme apenas o número da escolha.")
                continue
            
            if user_option == 1:
                #entrar num loop que abre um menu de compra de livros
                #primeiro exibe a lista de livros DISPONÍVEIS (adicionar coluna de disponibilidade e tirar quantidade nos livros)
                #depois escolhemos o livro pra comprar pelo id dele e então ou diminuimos a quantidade dele no banco ou tornamos ele indisponível
                #ao escolher um livro inserimos o cliente que comprou (usuario logado) na tabela de vendas
                #depois adicionamos o id do livro comprado na tabela de itens_venda com o id da venda que acabou de ser feita -> tirar duvida sobre isso
                pass
            elif user_option == 2:
                os.system("cls")
                titulo_de_busca = input("Pesquisar: ")
                resultados = buscar_livro_por_nome(titulo_de_busca)
                if resultados:
                    print("Resultados:\n")
                    for livro in resultados:
                        time.sleep(0.5)
                        print("------------------")
                        print(f"{livro[0]} -> {livro[1]}")
                        print("------------------")
                    input("\nPressione qualquer tecla para voltar ao menu...\n")
                    os.system("cls")
                else:
                    print("Não foi possível encontrar livros correspondentes")
                    input("\nPressione qualquer tecla para voltar ao menu\n")
                    os.system("cls")
            elif user_option == 3:
                os.system("cls")
                livros_cliente = listar_livros_usuario(user_logged[0])
                if livros_cliente:
                    print("Livros da sua coleção: \n")
                    for livro in livros_cliente:
                        print("------------------")
                        print(livro[0])
                        print("------------------")
                else:
                    print("Você ainda não possui livros na sua coleção")
                    input("\nPressione qualquer tecla para voltar ao menu...\n")
                    os.system("cls")
            