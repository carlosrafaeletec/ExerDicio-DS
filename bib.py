table = list()

dicio = {
    'nome': '',
    'idade': 0,
    'cpf': 0,
    'email': '',
    'telefone': 0
}

#exer 1
def PreencherTable(d: dict, t: list) -> None:
    while True:
        name = input("Nome: ")
        if  name == '.':
            break
        else:
            d['nome'] = name
            d['idade'] = input("Idade: ")
            d['cpf'] = input("cpf: ")
            d['email'] = input("seu email: ")
            d['telefone'] = input("Seu Telefone: ")
            t.append(d.copy())

#exer 2
def exibRegis(t: list, kei: int) -> None:
    i = 0
    
    for i in range(len(t)):
        if i == kei and kei >= 0:
            print(f"{t[i]}")
        else:
            i += 1

#exer 3
def exibTudo(t: list) -> None:
    if (t not in None):
        for i in range(len(t)):
            print(f"Nome: {t[i]['nome']}")
            print(f"Idade: {t[i]['idade']}")
            print(f"Cpf: {t[i]['cpf']}")
            print(f"Email: {t[i]['email']}")
    else:
        print("Você ainda não fez o cadastro!")

#Exer 4
def exibir_posicao(t: list, i: int) -> None:
    if i < len(t) and i >= 0:
        print(f"Nome...:{t[i]['nome']}") 
        print(f"E-mail.:{t[i]['email']}") 
    else:
        print("inexistente")

#Exer 5
def consultNome (t: list, n) -> None:
    for i in range(len(t)):
        if (n == t[i]['nome']):
            print(f"Nome: {t[i]['nome']}")
            print(f"E-mail: {t[i]['email']}")
        else:
            print("Inexistente")

# Exer 6
def consultado(t: list, n, d: dict) -> None:
    for i in range(len(t)):
        if (n == t[i]['nome']):
            print(f"Nome: {t[i]['nome']}")
            print(f"E-mail: {t[i]['email']}")
            print("\n ESTE REGISTRO JÁ EXISTE!! NÃO É POSSIVEL CADASTRAR")
        else:
            d['nome'] = n
            d['email'] = input("E-mail: ")
            d['idade'] = input("Idade: ")
            d['cpf'] = input("Cpf: ")
            d['telefone'] = input("Telefone: ")
            t.append(d)
             

#Exer 7
def editar(t: list, id: int) -> None:
    for i in range(len(t)):
        if (id == t[i]['cpf']):
            print(f"Cpf: {t[i]['cpf']}")
            print(f"Nome: {t[i]['nome']}")
            print(f"Telefone: {t[i]['telefone']}")
            print(f"E-mail: {t[i]['email']}")
            mod = input("\n Digite qual você quer modificar: ")

            if (mod == 'nome'):
                t[i]['nome'] = input("Digite outro nome: ")
            elif(mod == 'telefone'):
                t[i]['telefone'] = input("Digite outro telefone: ")
            elif(mod == 'email'):
                t[i]['email'] = input("Digite outro email: ")

#Exer 8
def excluir(t: list, id: int) -> None:
    for i in range(len(t)):
        if (id == t[i]['cpf']):
            print(f"Cpf: {t[i]['cpf']}")
            print(f"Nome: {t[i]['nome']}")
            print(f"Telefone: {t[i]['telefone']}")
            print(f"E-mail: {t[i]['email']}")
            exc = input("\n Confirma a exclusão? Digite [S]im ou [N]ão: ")

            if (exc.lower() == 's'):
                t[i].clear()
            elif (exc.lower() == 'n'):
                break