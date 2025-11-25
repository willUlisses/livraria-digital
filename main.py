from views.user_view import *
from pwinput import pwinput
from services.cliente_service import *
from services.livro_service import *
from services.editoras_service import *
from services.vendas_service import *
from services.autores_service import *
from exibicoes.mostrar_editoras import mostrar_editoras
from exibicoes.mostrar_autores import mostrar_todos_autores, mostrar_autores_buscados
from exibicoes.mostrar_livros import mostrar_livros_id_titulo, mostrar_livros_titulo, mostrar_livros_preco
from exibicoes.mostrar_vendas import exibir_vendas
import os
import sys
import time
from datetime import date

user_logged = None

while True:
    os.system("cls")
    login_user_panel()
    try:
        login_option = int(input("Informe o que quer fazer: "))
    except ValueError:
        os.system("cls")
        print("Você deve informar as opções apenas números.")
        continue    

    if login_option == 1:
        os.system("cls")

        print("Informe seus dados\n")
        email = input("Email: ")
        senha = pwinput("Senha: ")
        ja_existe = valida_registro(email)

        if ja_existe:
            os.system("cls")
            print(f"\nO email {email} já está cadastrado\n")
            time.sleep(1.5)
            continue

        registrar(email, senha)
        time.sleep(5)
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
    elif login_option == 0:
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

if user_logged:
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
                            case 1: #-------------------------------------> Adicionar livro
                                os.system("cls")
                                print("Informe os seguintes dados para o cadastro do livro:")
                                titulo = input("Título: ")
                                data_lancamento = input("Data de lançamento (AAAA-MM-DD): ")
                                try:
                                    valor_unitario = float(input("Valor unitário: "))
                                except ValueError:
                                    os.system("cls")
                                    print("Você deve informar apenas valores numéricos")
                                    input("Pressione qualquer tecla para voltar ao menu...")
                                    continue
                                if titulo and data_lancamento and valor_unitario:
                                    os.system("cls")
                                    tem_editora = input("O livro possui editora? [y/n]: ")
                                    if tem_editora.lower() == "y":
                                        while True:
                                            os.system("cls")
                                            print("Aqui estão as editoras existentes no sistema:\n")
                                            editoras = listar_editoras()
                                            mostrar_editoras(editoras)

                                            try:
                                                id_editora = int(input("Informe o identificador da editora do livro: "))
                                            except ValueError:
                                                os.system("cls")

                                            if id_editora and id_editora > 0:
                                                editora_existe = possui_editora(id_editora)
                                                if editora_existe:
                                                    id_livro = inserir_livro(titulo, data_lancamento, id_editora, valor_unitario)
                                                    break
                                                else:
                                                    os.system("cls")
                                                    print("Essa editora não está cadastrada no sistema, tente novamente")
                                                    time.sleep(2.0)
                                                    continue
                                            else: 
                                                os.system("cls")
                                                print("Você deve informar uma editora pelo menos.")
                                                time.sleep(2.0)
                                                continue

                                        os.system("cls")
                                        print("Agora informe o autor do livro\n")
                                        time.sleep(1.5)

                                        while True:
                                            autores = listar_todos_autores()
                                            if autores:
                                                os.system("cls")
                                                print("Abaixo estão listados os autores cadastrados:\n")
                                                mostrar_todos_autores(autores)
                                            else:
                                                os.system("cls")
                                                print("Ainda não há autores cadastrados no sistema, cadastre pelo menos um autor.")
                                                input("\nPressione qualquer tecla para sair...")
                                                break
                                            try:
                                                id_autor_livro = int(input("Informe o identificador do autor do livro em questão (Digite 0 para sair): "))
                                                
                                            except ValueError:
                                                os.system("cls")
                                                print("Você deve informar apenas valores numéricos")
                                                input("\nPressione qualquer tecla para voltar...")
                                                continue
                                            if id_autor_livro != 0 and id_autor_livro > 0:
                                                if tem_autor(id_autor_livro):
                                                    inserir_autor_livro(id_livro, id_autor_livro)
                                                    break
                                                else: 
                                                    os.system("cls")
                                                    print("Esse autor não está cadastrado no sistema, tente novamente...")
                                                    time.sleep(2.5)
                                                    continue
                                            else:
                                                print("Você deve escolher no mínimo um autor para cadastrar o livro!")
                                                input("\nPressione qualquer tecla para continuar...")
                                                continue
                                        
                                        os.system("cls")
                                        mais_autores = input("O livro possui mais de um autor? [Digite 'y' para confirmar ou qualquer tecla para continuar]: ")
                                        if mais_autores.lower() == "y":
                                            while True:
                                                autores = listar_todos_autores()
                                                if autores:
                                                    os.system("cls")
                                                    print("Abaixo estão listados os autores cadastrados:\n")
                                                    mostrar_todos_autores(autores)
                                               
                                                try:
                                                    id_autor_livro = int(input("Informe o identificador do autor do livro em questão (Digite 0 para sair): "))
                                                    
                                                except ValueError:
                                                    os.system("cls")
                                                    print("Você deve informar apenas valores numéricos")
                                                    input("\nPressione qualquer tecla para voltar...")
                                                    continue
                                                if id_autor_livro != 0:
                                                    inserir_autor_livro(id_livro, id_autor_livro)
                                                    continue
                                                else:
                                                    print("Voltando ao menu...")
                                                    input("\nPressione qualquer tecla para continuar...")
                                                    break
                                    elif tem_editora.lower() == "n":
                                        id_livro = inserir_livro_sem_editora(titulo, data_lancamento, valor_unitario)
                                        os.system("cls")
                                        print("Agora informe o autor do livro\n")
                                        time.sleep(1.5)

                                        while True:
                                            autores = listar_todos_autores()
                                            if autores:
                                                os.system("cls")
                                                print("Abaixo estão listados os autores cadastrados:\n")
                                                mostrar_todos_autores(autores)
                                            else:
                                                os.system("cls")
                                                print("Ainda não há autores cadastrados no sistema, cadastre pelo menos um autor.")
                                                input("\nPressione qualquer tecla para sair...")
                                                break
                                            try:
                                                id_autor_livro = int(input("Informe o identificador do autor do livro em questão (Digite 0 para sair): "))
                                                
                                            except ValueError:
                                                os.system("cls")
                                                print("Você deve informar apenas valores numéricos")
                                                input("\nPressione qualquer tecla para voltar...")
                                                continue
                                            if id_autor_livro != 0 and id_autor_livro > 0:
                                                if tem_autor(id_autor_livro):
                                                    inserir_autor_livro(id_livro, id_autor_livro)
                                                    continue
                                                else: 
                                                    os.system("cls")
                                                    print("Esse autor não está cadastrado no sistema, tente novamente...")
                                                    time.sleep(2.5)
                                                    continue
                                            else:
                                                os.system("cls")
                                                print("Você deve escolher no mínimo um autor para cadastrar o livro!")
                                                input("\nPressione qualquer tecla para continuar...")
                                                continue
                                        
                                        os.system("cls")
                                        mais_autores = input("O livro possui mais de um autor? [Digite 'y' para confirmar ou qualquer tecla para continuar]: ")

                                        if mais_autores.lower() == "y":
                                            while True:
                                                autores = listar_todos_autores()
                                                if autores:
                                                    os.system("cls")
                                                    print("Abaixo estão listados os autores cadastrados:\n")
                                                    mostrar_todos_autores(autores)
                                               
                                                try:
                                                    id_autor_livro = int(input("Informe o identificador do autor do livro em questão (Digite 0 para sair): "))
                                                    
                                                except ValueError:
                                                    os.system("cls")
                                                    print("Você deve informar apenas valores numéricos")
                                                    input("\nPressione qualquer tecla para voltar...")
                                                    continue
                                                if id_autor_livro != 0 and id_autor_livro > 0:
                                                    if tem_autor(id_autor_livro):
                                                        inserir_autor_livro(id_livro, id_autor_livro)
                                                        continue
                                                    else: 
                                                        os.system("cls")
                                                        print("Esse autor não está cadastrado no sistema, tente novamente...")
                                                        time.sleep(2.5)
                                                        continue
                                                else:
                                                    os.system("cls")
                                                    print("Voltando ao menu...")
                                                    input("\nPressione qualquer tecla para continuar...")
                                                    break
                                    else: 
                                        os.system("cls")
                                        print("Resposta inválida, tente o cadastro novamente")
                                        time.sleep(3)
                                        continue
                                    
                                    os.system("cls")
                                    print("Livro cadastrado com sucesso!")
                                    input("Pressione qualquer tecla para continuar...")    
                                else:
                                    os.system("cls")
                                    print("Você não pode deixar o título a data de lançamento nem o valor_unitario vazios, tente novamente")          
                                    input("\nPressione qualquer tecla para voltar ao menu...")
                                    continue
                                
                                os.system("cls")
                                input("Pressione qualquer tecla para continuar...")
                                continue
                                
                            case 2: # -------------------------------------- > remover livro (trocar para soft delete)
                                os.system("cls")
                                print("Aqui está a lista dos livros disponíveis no estoque:\n")
                                time.sleep(0.5)
                                livros_disponiveis = listar_todos_livros()
                                mostrar_livros_id_titulo(livros_disponiveis)
                                
                                try:
                                    id_para_remover = int(input("\nInforme o identificador do livro a ser removido: "))
                                except ValueError:
                                    os.system("cls")
                                    print("Você deve informar apenas valores númericos")
                                    input("Pressione qualquer botão para voltar ao menu")
                                    continue
                                
                                remover_livro_por_id(id_para_remover)
                                time.sleep(3)
                                continue
                           
                            case 3: #modificar titulo do livro 
                                os.system("cls")
                                print("Abaixo estão listados os livros do sistema: \n")
                                livros_disponiveis = listar_todos_livros()
                                mostrar_livros_id_titulo(livros_disponiveis)
                                
                                try:
                                    id_livro_modificado = int(input("Informe o identificador do livro que deseja alterar: "))
                                except ValueError:
                                    os.system("cls")
                                    print("Você deve informar apenas valores numéricos")
                                    input("\nPressione qualquer tecla para voltar...")
                                    continue
                                novo_titulo = input("Novo título: ")
                                os.system("cls")
                                alterar_titulo_livro(novo_titulo, id_livro_modificado)
                                input("\nPressione qualquer tecla para continuar")
                                continue
                            case 4:
                                os.system("cls")
                                titulo_do_livro = input("Informe o título do livro que deseja buscar: ")
                                resultados = buscar_livro_por_nome(titulo_do_livro)

                                print("Possíveis resultados: \n")
                                mostrar_livros_id_titulo(resultados)
                                
                                input("\nPressione qualquer tecla para continuar...")
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
                            case 2: # ----------------------------------------------------------------> deletar editora (soft delete)
                                os.system("cls") 
                                print("Aqui estão as editoras existentes no sistema:\n")
                                editoras_existentes = listar_editoras()
                                time.sleep(0.7)

                                mostrar_editoras(editoras_existentes)

                                try:
                                    id_editora_escolhida = int(input("Informe o id da editora a ser removida ou digite 0 para sair:\n"))
                                except ValueError:
                                    os.system("cls")
                                    print("Você deve digitar apenas valores númericos")
                                    continue
                                if id_editora_escolhida != 0:
                                    remover_editora_por_id(id_editora_escolhida)
                                    print("A editora foi removida com sucesso do sistema!\n")
                                    input("Pressione qualquer tecla para continuar...")
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
                                    mostrar_editoras(editoras_no_sistema)
                                    
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
                                os.system("cls")
                                print("Informe os seguintes dados para cadastrar um novo autor no sistema: ")
                                nome_autor = input("Nome: ")
                                nacionalidade_autor = input("Nacionalidade [Pressione Enter caso não queria informar]: ")
                                if nome_autor:
                                    inserir_autor(nome_autor, nacionalidade_autor)
                                    print("Autor inserido com sucesso! voltando ao menu...")
                                    time.sleep(2)
                                    continue
                                else:
                                    os.system("cls")
                                    print("Você deve inserir no mínimo o nome do autor para cadastrá-lo")
                                    input("\nPressione qualquer tecla para continuar...")
                                    continue
                            case 2:
                                os.system("cls")
                                print("Abaixo estão listados os autores cadastrados no sistema:")
                                autores_ativos = listar_todos_autores()
                                mostrar_todos_autores(autores_ativos) 
                                try:
                                    id_autor_removido = int(input("Informe o id do autor para remover: "))
                                except ValueError:
                                    os.system("cls")
                                    print("Você deve informar apenas valores numéricos.")
                                    input("\nPressione qualquer tecla para continuar...")
                                    continue  

                                if id_autor_removido and id_autor_removido > 0:
                                        if tem_autor(id_autor_removido):
                                            remover_autor_por_id(id_autor_removido)
                                            print("Autor removido com sucesso! voltando ao menu...")
                                            time.sleep(2)
                                            continue
                                        else:
                                            os.system("cls")
                                            print(f"O autor com ID {id_autor_removido} não está cadastrado no sistema, tente novamente")  
                                            time.sleep(2)
                                            continue                                  
                            case 3: 
                                os.system("cls")
                                print("Abaixo estão listados os autores cadastrados no sistema:")
                                autores_ativos = listar_todos_autores()
                                mostrar_todos_autores(autores_ativos)
                                try:
                                    id_autor_modificado = int(input("Informe o ID do autor que deseja modificar: "))
                                except ValueError:
                                    os.system("cls")
                                    print("Você deve informar apenas valores numéricos")
                                    input("\nPressione qualquer tecla para continuar")
                                    continue

                                if id_autor_modificado and id_autor_modificado > 0:
                                    if tem_autor(id_autor_modificado):
                                        os.system("cls")
                                        novo_nome_autor = input("Informe o novo nome do autor: ")                                        
                                        modificar_nome_autor(novo_nome_autor, id_autor_modificado)
                                        print(f"Nome do autor de ID {id_autor_modificado} modificado para: {novo_nome_autor}")
                                        time.sleep(2.5)
                                        continue
                                    else:
                                        os.system("cls")
                                        print("Esse autor não está cadastrado no sistema, tente novamente...")
                                        input("\nPressione qualquer tecla para continuar...")
                                        continue
                            case 4:
                                os.system("cls")
                                print("Informe o nome do autor para pesquisar")
                                nome_autor_busca = input("Pesquisar: ")

                                os.system("cls")
                                if nome_autor_busca:
                                    resultados = buscar_autor_por_nome(nome_autor_busca)
                                    print("Abaixo estão os possíveis resultados: \n")

                                    if resultados:
                                        mostrar_autores_buscados(resultados)
                                    else:
                                        print("Nenhum autor corresponde à sua pesquisa.")

                                    input("\nPressione qualquer tecla para continuar")
                                    continue
                                else:
                                    print("Você deve informar no mínimo uma letra para que a pesquisa seja bem sucedida.")
                                    input("\nPressione qualquer tecla para continuar...")
                                    continue
                            case 0:
                                os.system("cls")
                                print("Voltando para o menu inicial...")
                                time.sleep(1.5)
                                break 
                            case _:
                                os.system("cls")
                                print("Digite uma opção válida.")
                                time.sleep(1.5)
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
                            case 1: #--------------------------------------------------> Cadastrar Venda
                                os.system("cls")
                                while True:
                                    print("Aqui está a lista dos livros disponíveis:\n")
                                    time.sleep(0.5)
                                    livros_disponiveis = listar_todos_livros()
                                    mostrar_livros_preco(livros_disponiveis)
                                    try:
                                        id_livro_escolhido = int(input("\nEscolha o id do livro que deseja comprar ou digite 0 para voltar ao menu:\n"))
                                        if id_livro_escolhido != 0 and id_livro_escolhido > 0:
                                            os.system("cls")
                                            livro_escolhido = buscar_livro_por_id(id_livro_escolhido)
                                            if livro_escolhido:
                                                print(f"O livro escolhido foi: {livro_escolhido[1]}\n")
                                                quantidade = int(input("Informe quantas cópias deseja comprar: "))
                                            else:
                                                os.system("cls")
                                                print("Esse livro não está cadastrado no sistema, tente novamente")
                                                time.sleep(2.5)
                                                continue
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
                            case 2:
                                os.system("cls")
                                print("Abaixo estão as vendas cadastradas no sistema: \n")
                                vendas_cadastradas = listar_vendas()
                                exibir_vendas(vendas_cadastradas)
                                
                                input("\nPressione qualquer tecla para continuar...")
                                continue
                            case 3: #remover uma venda junto aos seus itens venda (hard delete on cascade all com itens_venda)
                                os.system("cls")
                                print("Abaixo estão as vendas cadastradas no sistema: \n")
                                vendas_cadastradas = listar_vendas()
                                exibir_vendas(vendas_cadastradas)

                                try:
                                    id_venda_removida = int(input("Informe o id da venda a ser removida ou digite 0 para sair: "))
                                    if id_venda_removida != 0 and id_venda_removida > 0:
                                        if possui_venda(id_venda_removida):
                                            remover_venda_por_id(id_venda_removida)
                                            os.system("cls")
                                            print("Venda removida com sucesso!")
                                            input("Pressione qualquer tecla para continuar...")
                                            continue
                                        else:
                                            os.system("cls")
                                            print("A venda a ser removida não está cadastrada no sistema, tente novamente")
                                            time.sleep(2)
                                            continue
                                    elif id_venda_removida == 0:
                                        os.system("cls")
                                        print("Voltando ao menu anterior...")
                                        time.sleep(2)
                                        continue
                                    else:
                                        print("\nInforme um valor válido!")
                                        time.sleep(1.5)
                                        continue
                                except ValueError:
                                    os.system("cls")
                                    print("Informe apenas valores numéricos.")
                                    input("Pressione qualquer tecla para continuar...")
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
                elif admin_option == 0:
                    os.system("cls")
                    print("Saindo do sistema:")
                    time.sleep(1.5)
                    sys.exit(0)
        else: # -------------------> para o caso de ser um usuário normal
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
                        mostrar_livros_preco(livros_disponiveis)
                        
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
                        mostrar_livros_id_titulo(resultados)
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
                        mostrar_livros_titulo(livros_cliente)
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
else:
    print(" \nUsuário não encontrado no sistema, tente novamente.\n")