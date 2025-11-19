from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *
from services.livro_service import *
from services.editoras_service import *
from services.vendas_service import *
import os
import sys
import time
from datetime import date
from psycopg2.errors import ForeignKeyViolation



user_logged = None

while True:
    login_user_panel()
    try:
        login_option = int(input("Informe o que quer fazer: "))
    except ValueError:
        os.system("cls")
        print("Você 3pode informar as opções apenas com números.")
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
            os.system("cls")
            admin_option_panel()
            try:
                admin_option = int(input("\nDigite a opção: "))
            except ValueError:
                os.system("cls")
                print("Você deve digitar apenas números.")
                continue
            if admin_option == 1: # ----------------------------------------------------- Livros
                os.system("cls")
                while True:
                    os.system("cls")
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
                            pass #------------------> Adicionar livro
                        case 2:
                            os.system("cls")
                            print("Aqui está a lista dos livros disponíveis no estoque:\n")
                            time.sleep(0.5)
                            livros_disponiveis = listar_todos_livros()
                            
                            for livro in livros_disponiveis:
                                time.sleep(0.7)
                                print("------------------")
                                print(f"{livro[0]} -> {livro[1]}")
                                print("------------------")
                            
                            try:
                                id_para_remover = int(input("\nInforme o identificador do livro a ser removido: "))
                            except ValueError:
                                os.system("cls")
                                print("Você deve informar apenas valores númericos")
                                input("Pressione qualquer botão para voltar ao menu")
                                continue
                            
                            remover_livro_por_id(id_para_remover)
                            continue
                        case 3: 
                            pass #modificar titulo do livro
                        case 4:
                            os.system("cls")
                            titulo_do_livro = input("Informe o título do livro que deseja buscar: ")
                            resultados = buscar_livro_por_nome(titulo_do_livro)

                            print("Possíveis resultados: ")
                            for livro in resultados:
                                time.sleep(0.7)
                                print("------------------")
                                print(f"Id: {livro[0]} -> Título: {livro[1]}")
                                print("------------------")

                        case 0:
                            os.system("cls")
                            print("Voltando para o menu inicial...")
                            time.sleep(1.5)
                            break
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
            elif admin_option == 2: # ---------------------------------------------------- editoras
                while True:
                    os.system("cls")
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
                            os.system("cls") 
                            print("Aqui estão as editoras existentes no sistema:\n")
                            editoras_existentes = listar_editoras()
                            time.sleep(0.7)

                            for editora in editoras_existentes:
                                time.sleep(0.7)
                                print("------------------")
                                print(f"{editora[0]} -> {editora[1]}")
                                print("------------------")

                            try:
                                id_editora_escolhida = int(input("Informe o id da editora a ser removida ou digite 0 para sair:\n"))
                            except ValueError:
                                os.system("cls")
                                print("Você deve digitar apenas valores númericos")
                                continue
                            if id_editora_escolhida != 0:
                                try:
                                    remover_editora_por_id(id_editora_escolhida)
                                    print("A editora foi removida com sucesso do sistema!\n")
                                    input("Pressione qualquer tecla para continuar...")
                                except ForeignKeyViolation:
                                    os.system("cls")
                                    print("Não é possível excluir uma editora associada à um ou mais livros, tente excluir o livro primeiro!")
                                    input("\nPressione qualquer tecla para voltar ao menu...")
                                    continue
                            else:
                                os.system("cls")
                                print("Voltando ao menu principal...")
                                time.sleep(1.5)
                                break
                        case 3: 
                            os.system("cls")
                            editoras_no_sistema = listar_editoras()

                            if editoras_no_sistema:
                                print("Essas são as editoras presentes no sistema:\n")

                                for editora in editoras_no_sistema:
                                     time.sleep(0.7)
                                     print("------------------")
                                     print(f"Id: {editora[0]} -> Nome: {editora[1]}")
                                     print("------------------")
                                
                                try:
                                    id_editora_para_editar = int(input("Digite o id da editora que deseja modificar ou digite 0 para voltar ao menu: \n"))
                                    os.system("cls")
                                    novo_nome = input("Informe o nome que deseja por nessa editora: ")
                                    alterar_nome_editora(novo_nome, id_editora_para_editar)
                                    print("Editora modificada com sucesso!")
                                    input("\nPressione qualquer tecla para continuar...")
                                except ValueError:
                                    os.system("cls")
                                    print("Informe apenas valores numéricos.")
                                    input("Pressione qualquer tecla para voltar ao menu...")
                                    continue
                        case 4:
                            os.system("cls")
                            print("Informe o nome da editora que deseja encontar:")
                            nome_de_busca = input("Pesquisar: ")
                            resultados = buscar_editora_por_nome(nome_de_busca)

                            if resultados:
                                os.system("cls")
                                print("Possíveis resultados:\n")
                                for editora in resultados:
                                    time.sleep(0.7)
                                    print("------------------")
                                    print(f"Nome: {editora[0]} -> Cidade: {editora[1]}")
                                    print("------------------")
                                
                                input("\nPressione qualquer tecla para voltar ao menu...")
                            else:
                                os.system("cls")
                                print("Não foi possível encontrar nenhum resultado compatível com sua busca")
                                input("Pressione qualquer tecla para voltar ao menu...")
                                continue
                        case 0:
                            os.system("cls")
                            print("Voltando para o menu inicial...")
                            time.sleep(1.5)
                            break 
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
            elif admin_option == 3: # -------------------------------------------------------------------- Autores
                while True:
                    os.system("cls")
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
                        case 0:
                            os.system("cls")
                            print("Voltando para o menu inicial...")
                            time.sleep(1.5)
                            break 
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
            elif admin_option == 4: # ---------------------------------------------------------------- Vendas
                while True:
                    os.system("cls")
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
                        case 0:
                            os.system("cls")
                            print("Voltando para o menu inicial...")
                            time.sleep(1.5)
                            break  
                        case _:
                            os.system("cls")
                            print("Digite uma opção válida.")
                            continue
            elif admin_option == 0:
                os.system("cls")
                print("Saindo do sistema:")
                time.sleep(1.5)
                sys.exit(0)
    else: #para o caso de ser um usuário normal
        while True:
            os.system("cls")
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
                        id_livro_escolhido = int(input("\nEscolha o id do livro que deseja comprar ou digite 0 para voltar ao menu:\n"))
                        if id_livro_escolhido != 0:
                            os.system("cls")
                            livro_escolhido = buscar_livro_por_id(id_livro_escolhido)
                            print(f"O livro escolhido foi: {livro_escolhido[1]}\n")
                            quantidade = int(input("Informe quantas cópias deseja comprar: "))
                        else:
                            os.system("cls")
                            print("\nVoltando ao menu inicial...")
                            time.sleep(1.5)
                            break
                    except ValueError:
                        os.system("cls")
                        print("Você deve digitar apenas valores numéricos.")
                        continue
                    valor_total = quantidade * livro_escolhido[2]
                    id_venda_feita = inserir_venda(user_logged[0], date.today(), valor_total)
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
                        time.sleep(0.7)
                        print("------------------")
                        print(f"Título: {livro[0]}")
                        print("------------------")
                    input("\nPressione qualquer tecla para prosseguir...")

                else:
                    print("Você ainda não possui livros na sua coleção.")
                    input("\nPressione qualquer tecla para voltar ao menu...\n")
                    os.system("cls")
            elif user_option == 0:
                os.system("cls")
                print("Saindo do sistema:")
                time.sleep(1.5)
                sys.exit(0)