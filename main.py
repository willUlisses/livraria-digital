from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *
from services.livro_service import *
from services.editoras_service import *
from services.vendas_service import *
import os
import sys
import time
from datetime import date, datetime

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

                    match(livros_option):
                        case 1:
                            pass #Adicionar livro
                        case 2:
                            pass #remover livro
                        case 3: 
                            pass #modificar titulo do livro
                        case 4:
                            pass #buscar por nome do livro
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
            elif admin_option == 2:
                os.system("cls")
                while True:
                    admin_editoras_panel()
                    try:
                        editoras_option = int(input("Digite sua opção: "))
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas números.")
                        time.sleep(1)
                        continue
                        
                    match(editoras_option):
                        case 1:
                            os.system("cls")
                            print("Informe os seguintes dados da editora para cadastrá-la:\n")
                            nome = input("Nome: ")
                            cidade = input("Cidade: ")
                            inserir_editora(nome, cidade)
                            continue
                        case 2:
                            pass #remover 
                        case 3: 
                            pass #modificar 
                        case 4:
                            pass #buscar por nome
                        case 5:
                            os.system("cls")
                            break 
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
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
                        
                    match(autores_option):
                        case 1:
                            pass #Adicionar 
                        case 2:
                            pass #remover 
                        case 3: 
                            pass #modificar 
                        case 4:
                            pass #buscar por nome 
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
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
                    
                    match(vendas_option):
                        case 1:
                            pass #Cadastrar 
                        case 2:
                            pass #Listar  
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
    else: #para o caso de ser um usuário normal
        while True:
            user_options_panel()
            try:
                user_option = int(input("Informe sua opçao: "))
            except ValueError:
                print("\nInforme apenas o número da escolha.")
                continue
            
            if user_option == 1:
                os.system("cls")
                while True:
                    print("Aqui está a lista dos livros disponíveis:\n")
                    time.sleep(0.5)
                    livros_disponiveis = listar_todos_livros()
                    
                    for livro in livros_disponiveis:
                        time.sleep(0.7)
                        print("------------------")
                        print(f"{livro[0]} -> {livro[1]} - R${livro[2]}")
                        print("------------------")
                    
                    try:
                        id_livro_escolhido = int(input("\nEscolha o livro que deseja comprar pelo id dele:\n"))
                        os.system("cls")
                        livro_escolhido = buscar_livro_por_id(id_livro_escolhido)
                        print(f"O livro escolhido foi: {livro_escolhido[1]}\n")
                        quantidade = int(input("Informe quantas cópias deseja comprar: "))
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas valores numéricos.")
                        continue
                    valor_total = quantidade * livro_escolhido[4]
                    id_venda_feita = inserir_venda(user_logged[0], date.now(), valor_total)
                    cadastrar_item_venda(id_venda_feita, livro_escolhido[0], quantidade) 
                    os.system("cls")
                    print("Compra finalizada com sucesso, aqui estão os dados da sua compra:\n")
                    print(f"Título: {livro_escolhido[1]}\nQuantidade: {quantidade}\nTotal: {valor_total}")
                    input("\nPressione qualquer botão para prosseguir...")                   
                    break 
                
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