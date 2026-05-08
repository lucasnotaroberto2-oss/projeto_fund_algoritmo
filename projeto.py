import ast
pular_linha = ("------------------------------x------------------------------")
#--------cadastro---------------------------------------------------------------------------
def novo_usuario() :
    nome = input ("digite seu nome...: ")
    email = input("digite seu email..: ")
    senha = input("digite sua senha..: ")
    usuario = {"nome" : nome,
               "email" : email,
               "senha" : senha}
    return usuario

def criar_lista_usuarios() :
    usu = []
    arquivo = open("usuarios.txt","r")
    for i in arquivo.readlines():
        usu.append(i)
    return usu

def adicionar_usuario(usuario_criado) :
    usuarios = criar_lista_usuarios()
    usuarios.append(usuario_criado)
    arquivo = open("usuarios.txt","w")
    for i in usuarios:
        arquivo.write(str(i) + "\n")
    arquivo.close()

#--------login------------------------------------------------------------------------------

def checagem_login() :
    email = input("digite seu email..: ")
    senha = input("digite sua senha..: ")
    usuarios = criar_lista_usuarios()
    for usuario in range (len(usuarios)):
        usuario_dict = ast.literal_eval(usuarios[usuario])
        if usuario_dict['email'] == email and usuario_dict['senha'] == senha:
            print("Usuário logado! Bem-vindo!")
            return usuario_dict
    print("Usuário não encontrado... tente novamente!")
    return False

#---------filmes----------------------------------------------------------------------------

def catalogo():
    l = []
    arquivo = open("filmes.txt","r")
    arquivo.seek(0)
    for linha in arquivo.readlines():
        l.append(linha)
        print(linha)
    arquivo.close()
    return l

def procura_filme(filme,cat):
    if 1 <= filme <= len(cat):
        print(cat[filme - 1])
    else:
        print("filme invalido!")
    return cat[filme - 1]

def criar_filme_favoritos():
    fil = []
    arquivo = open("lista_favoritos.txt","r")
    for i in arquivo.readlines():
        fil.append(i.strip()) #o strip remove elementos invisiveis do texto, como espaços em branco ou linhas desnecessarias
    arquivo.close()
    return fil

def ad_filme_lista(num_filme,filme_achado,usuario_logado):
    film = carregar_lista_favoritos()
    for filme in film:
        filme_dict = ast.literal_eval(filme)
        if filme_dict['email'] == usuario_logado['email'] and filme_dict['numero'] == num_filme:
            print("esse filme ja esta na sua lista!")
            return
    f = {
        "email":usuario_logado['email'],
        "numero":num_filme,
        "filme":filme_achado.strip()
        }
    film.append(f)
    arquivo = open("lista_favoritos.txt","w")
    for i in film:
        arquivo.write(str(i).strip() + "\n")
    print("filme adicionado!")
    arquivo.close()
    return f
#-------gerenciamento da lista de favoritos-------------------------------------------------

def catalogo_lista_favoritos(usuario_logado):
    arquivo = open("lista_favoritos.txt","r")
    for i in arquivo.readlines():
        filme = ast.literal_eval(i.strip())
        if filme['email'] == usuario_logado['email']:
            print(filme)
    arquivo.close()
    return

def carregar_lista_favoritos():
    l = []
    arquivo = open("lista_favoritos.txt","r")
    for i in arquivo.readlines():
        l.append(ast.literal_eval(i.strip())) #o ast literal eval transforma as linhas em listas com dicionarios
    arquivo.close()
    return l

def excluir_filme(filme_excluido):
    l_favs = carregar_lista_favoritos()
    nova_lista = []
    for filme in l_favs:
        if filme['numero'] != filme_excluido:
            nova_lista.append(filme)
    arquivo = open("lista_favoritos.txt", "w")
    for filme in nova_lista:
        arquivo.write(str(filme).strip() + "\n")
    arquivo.close()
    print("filme removido da lista de favoritos!")

#-------codigo principal--------------------------------------------------------------------

inicio = input("digite 1 para cadastro, 2 para login ou enter para sair..: ")
if inicio == "1" or inicio == "2":
    if inicio == "1":
        usuario_criado = novo_usuario()
        adicionar_usuario(usuario_criado)
        print("usuario criado com sucesso!")
        print(pular_linha)
    while True:
        usuario_logado = checagem_login()
        if usuario_logado:
            break
        print(pular_linha)
    while True:
        print(pular_linha)
        gerencia = input("digite 1 para pesquisar, 2 para gerenciariamento e 3 para sair..: ")
        print(pular_linha)
        if gerencia == "1":
            cat = catalogo()
            print(pular_linha)
            num_filme = int(input("digite o numero do filme dentro do nosso catalogo(1 a 30)..: "))
            print(pular_linha)
            filme_achado = procura_filme(num_filme,cat)
            print(pular_linha)
            x = input("digite 1 para adicionar filme aos favoritos ou enter para sair..: ")
            print(pular_linha)
            if x == "1":
                ad_filme_lista(num_filme,filme_achado,usuario_logado)
        elif gerencia == "2":
            catalogo_lista_favoritos()
            print(pular_linha)
            exclusao = input("digite 1 para excluir um filme da lista de favoritos ou enter para sair..: ")
            print(pular_linha)
            if exclusao == "1":
                filme_excluido = int(input("qual filme quer excluir da lista? "))
                print(pular_linha)
                excluir_filme(filme_excluido)
                print(pular_linha)
        elif gerencia == "3":
            print(pular_linha)
            print("obrigado por usar nosso programa!")
            break
else:
    print(pular_linha)
    print("obrigado por usar nosso programa!")    

#lista de coisas a fazer:
# 1 - resolver o bug de adicionar filme aos favoritos