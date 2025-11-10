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
        break
    else: #para o caso de ser um usuário normal
        while True:
            user_options_panel()
            try:
                user_option = int(input("Informe sua opçao:"))
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
                    print("Resultados possíveis:\n")
                    for livro in resultados:
                        time.sleep(3)
                        print("------------------")
                        print(f"{livro[0]} -> {livro[1]}")
                else:
                    print("Não foi possível encontrar livros correspondentes")
            elif user_option == 3:
                os.system("cls")
                livros_cliente = listar_livros_usuario()
                if livros_cliente:
                    print("Livros da sua coleção: \n")
                    for livro in livros_cliente:
                        print("------------------")
                        print(livro[0])
                else:
                    print("Você ainda não possui livros na sua coleção")
            