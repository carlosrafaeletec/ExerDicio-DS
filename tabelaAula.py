import os
'''
tabela = list()
# forma 1
# contato = dict()
# contato['nome'] = ''
# contato['telefone'] = ''
# contato["idade"] = 0

# forma 2
contato = {
    "nome": "",
    "telefone": "",
    "idade": 0
}

# preenchendo um registro
contato["nome"] = input("Nome: ")
contato["telefone"] = input("Telefone: ")
contato["idade"] = input("Idade: ")
tabela.append(contato.copy())


contato["nome"] = input("Nome: ")
contato["telefone"] = input("Telefone: ")
contato["idade"] = input("Idade: ")
tabela.append(contato)


print(tabela)

for i in range(0, len(tabela), 1):
    print(f"Nome...: {tabela[i]['nome']}")
    print(f"telefone...: {tabela[i]['telefone']}")
    print(f"idade...: {tabela[i]['idade']}")

print(tabela)
'''
#Exercicios 

#exer 1
table = list()

dicio = {
    'nome': ''
    'idade': 0
    'elo': ''
    'nivel': ''
}

def PreencherTable(d: dict, t: list) -> None:
    while True:
        d['nome'] = input("Nome: ")
        d['idade'] = input("Idade: ")
        d['elo'] = input("Elo: ")
        d['nivel'] = input("Nivel: ")

        if d['nome'] != '.'
            t.append(d.copy())
        else:
            break

def exibRegis(t: list) -> None:
    ind = input("Digite qual indice deseja ver")
    i = 0

    for i in range(len(t)):
        if i == ind:
            print(t[i])
        else:
            i += 1

def exibTudo(t: list) -> None:
    for i in range(len(t)):
        print(f"Nome: {t[i]['nome']}")
        print(f"Idade: {t[i]['idade']}")
        print(f"Elo: {t[i]['elo']}")
        print(f"Nivel: {t[i]['nivel']}")

PreencherDicio(dicio, table)
exibRegis(table)
exibTudo(table)

