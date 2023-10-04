import os
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
            
            # Cenário 1 - Sucesso
            Digite um nome: Edson

            Nome: Edson
            E-mail: eds@eds.com 
            -------------------------------------------
            # Cenário 2 - insucesso
            Digite um nome: Estela
            
            Inexistente

        6 - Cadastrar consultando
            # Cenário 1
            Nome: Edson

            Nome: Edson
            E-mail: eds@eds.com 
            ESTE REGISTRO JÁ EXISTE!! NÃO É POSSIVEL CADASTRAR

            # Cenário 2
            Nome: Maria
            E-mail: ..............
    """)

    op = int(input("\nDigite sua opcao: "))
    match(op):
        case 1:
            PreencherTable(dicio, table)

        case 2:
            kei = int(input("Digite qual key deseja ver: "))
            exibRegis(table, kei)

        case 3:
            exibTudo(table)

        case 4:
            ind = int(input("Posição: "))
            exibir_posicao(tabela, ind)
        
        case 5:
            
        
        case 6:


        case 0:
            print("\nDesligando\n")
            break

            