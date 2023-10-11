
from bib import *
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

while True:
    print("""
        0 - Sair
        1 - Cadastrar 
        2 - Listar
        3 - Cadastrar multiplos (até que seja digitado.)
        4 - Exibir um específico
        5 - Consultar por nome (ou outra chave unica)
        6 - Cadastrar consultando
        7 - Editar 
        8 - Excluir
    """)

    op = int(input("\nDigite sua opcao: "))
    match(op):
        case 1:
            PreencherTable(dicio, table)

        case 2:
            kei = int(input("\n Digite qual key deseja ver: "))
            exibRegis(table, kei)

        case 3:
            exibTudo(table)

        case 4:
            ind = int(input("\n Posição: "))
            exibir_posicao(table, ind)
        
        case 5:
            name = input("\n Digite seu nome: ")
            consultNome(table, name)
        
        case 6:
            name = input("\n Nome: ")
            consultado(table, name, dicio)

        case 7:
            id = input("Cpf: ")
            editar(table, id)

        case 8:
            id = input("CPF: ")
            excluir(table, id)

        case 0:
            print("\nDesligando\n")
            break

            