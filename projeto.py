#parte 1 do projeto - definição de interface inicial(login/cadastro)
x = "-----x-----"
print(x)
inicio = input("digite 1 para cadastro, 2 para login ou enter para sair..: ")
print(x)
l = []
if inicio == "1" or inicio == "2":
    if inicio == "1":
        nome = input    ("informe seu nome......: ")
        endereco = input("informe seu endereço..: ")
        telefone = input("informe seu telefone..: ")
        email = input   ("informe seu e-mail....: ")
        senha = input   ("informe sua senha.....: ") 
        #bloco para adicionar senha e email em um arquivo de texto
    elif inicio == "2":
        while True:
            email = input   ("informe seu e-mail....: ")
            senha = input   ("informe sua senha.....: ")
            if email in l and senha in l:
                #a lista vazia será trocado pelo arquivo de texto correspondente
                print(x)
                print("acesso permitido!")
                break
            else:
                print(x)
                print("acesso negado, tente novamente!")
else:
    print("obrigado por usar nosso programa!")     