
table = list()

dicio = {
    'nome': '',
    'idade': 0,
    'elo': '',
    'nivel': ''
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
            d['elo'] = input("Elo: ")
            d['nivel'] = input("Nivel: ")
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
    for i in range(len(t)):
        print(f"Nome: {t[i]['nome']}")
        print(f"Idade: {t[i]['idade']}")
        print(f"Elo: {t[i]['elo']}")
        print(f"Nivel: {t[i]['nivel']}")

#Exer 4
def exibir_posicao(t: list, i: int) -> None:
    if i < len(t) and i >= 0:
        print(f"Nome...:{t[i]['nome']}") 
        print(f"E-mail.:{t[i]['email']}") 
    else:
        print("inexistente")

#Exer 5
    print("O Rafa torce para o santos")
