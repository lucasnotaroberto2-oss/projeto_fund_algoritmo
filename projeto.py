#parte 1 do projeto - definição de interface inicial(cadastro/login)

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
    arquivo = open("usuarios.txt","r")
    arquivo.seek(0)
    conteudo = arquivo.read()
    arquivo.close()
    if conteudo == "":
        return []
    return eval(conteudo)

def adicionar_usuario(usuario_criado) :
    usuarios = criar_lista_usuarios()
    usuarios.append(usuario_criado)
    arquivo = open("usuarios.txt","w")
    arquivo.write(str(usuarios))
    arquivo.close()

#--------login------------------------------------------------------------------------------

def login_usuario() :
    email = input("digite seu email..: ")
    senha = input("digite sua senha..: ")
    return email,senha

def checagem_sim(usuario_logado) :
    
#-------------------------------------------------------------------------------------------

inicio = input("digite 1 para cadastro, 2 para login ou enter para sair..: ")
if inicio == "1" or inicio == "2":
    if inicio == "1":
        usuario_criado = novo_usuario()
        adicionar_usuario(usuario_criado)
        print("usuario criado com sucesso!")
    usuario_logado = login_usuario()
    while True:
        if checagem_sim(usuario_logado):
            print("usuario logado, bem vindo ao programa!")
            break
        else:
            print("usuario não encontrado no sistema, tente novamente!")
else:
    print("obrigado por usar nosso programa!")     