#parte 1 do projeto - definição de interface inicial(login/cadastro)
def novo_usuario() :
    usuario = []
    nome = input ("digite seu nome...: ")
    email = input("digite seu email..: ")
    senha = input("digite sua senha..: ")
    usuario.append(nome)
    usuario.append(email)
    usuario.append(senha)
    return usuario

def usuarios(usuario_criado) :
    arquivo = open("usuarios.txt", "a")
    arquivo.write(str(usuario_criado))
    arquivo.close()

inicio = input("digite 1 para cadastro, 2 para login ou enter para sair..: ")
if inicio == "1" or inicio == "2":
    if inicio == "1":
        usuario_criado = novo_usuario()
        usuarios(usuario_criado)
    print("acesso permitido...")
else:
    print("obrigado por usar nosso programa!")     