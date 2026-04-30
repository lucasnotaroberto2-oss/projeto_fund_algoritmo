#parte 1 do projeto - definição de interface inicial(cadastro/login)

import ast

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
        arquivo.write("\n%s" %i)
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
            arquivo = open("filmes_usuarios.txt","w")
            return True
        
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

def procura_filme(filme,f):
    if 1 <= filme <= len(f):
        print(f[filme - 1])
    else:
        print("filme invalido!")

#-------codigo principal--------------------------------------------------------------------

inicio = input("digite 1 para cadastro, 2 para login ou enter para sair..: ")
if inicio == "1" or inicio == "2":
    if inicio == "1":
        usuario_criado = novo_usuario()
        adicionar_usuario(usuario_criado)
        print("usuario criado com sucesso!")
    while True:
        if checagem_login():
            break
    while True:
        gerencia = input("digite 1 para pesquisar, 2 para gerenciariamento e 3 para sair..: ")
        if gerencia == "1":
            f = catalogo()
            filme = int(input("digite o numero do filme dentro do nosso catalogo(1 a 30)..: "))
            procura_filme(filme,f)
        elif gerencia == "3":
            print("obrigado por usar nosso programa!")
            break
else:
    print("obrigado por usar nosso programa!")     