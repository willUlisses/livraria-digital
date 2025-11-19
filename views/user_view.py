
def login_user_panel():
    print("=== BEM VINDO ===")
    print("\n1 - Registrar-se\n2 - Entrar\n0 - Sair")

def user_options_panel():
    print("=== MENU DO USUARIO\n")
    print("1- Comprar um Livro\n2 - Buscar Livro\n3 - Listar Seus Livros\n0 - Sair")

def admin_option_panel():
    print("BEM VINDO!\nEscolha o que deseja modificar:\n")
    print("1 - Livros\n2 - Editoras\n3 - Autores\n4 - Vendas\n0 - Sair do Sistema") #considerar opção para atuar com clientes

def admin_livros_panel():
    print("O que você deseja modificar nos livros?\n")
    print("1 - Adicionar um livro\n2 - Remover um livro\n3 - Modificar um livro\n4 - Buscar Livros\n0 - Voltar ao inicio")
    
def admin_editoras_panel():
    print("O que você deseja modificar nas editoras?\n")
    print("1 - Adicionar uma editora\n2 - Remover uma editora\n3 - Alterar nome da editora\n4 - Buscar Editoras\n0 - Voltar ao inicio")

def admin_autores_panel():
    print("O que você deseja modificar nos autores?")
    print("1 - Cadastrar novo autor\n2 - Remover um autor\n3 - Alterar nome do autor\n4 - Buscar Autor\n0 - Voltar ao inicio")

def admin_vendas_panel():
    print("O que você deseja realizar nas vendas?")
    print("1 - Cadastrar nova venda\n2 - Listar vendas realizadas\n0 - Voltar ao inicio")

def admin_clientes_panel():
    print("O que você deseja fazer quanto aos clientes?")
    print("1 - Buscar por Cliente\n2 - Listar compras de um cliente\n0 - Voltar ao inicio")