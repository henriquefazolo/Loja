disponiveis = ['JOGO TESTE']
preco_venda = [50.99]
qtd_disponivel = [5]
preco_fabrica = [23.50]
vendas = [0]
compras = [0]

while True:
    print('1 - Registrar venda.')
    print('2 - Compra de estoque.')
    print('3 - Resumo da loja.')
    print('4 - Sair')

    opcao = int(input('Insira a opção desejada : '))
    if opcao == 4:
        print('Caixa Fechado')
        break

    elif opcao == 3:
        print('DISPONIVEIS'.ljust(22, ' '),
              'PREÇO DE VENDA'.ljust(22, ' '),
              'QUANTIDADE DISPONIVEL'.ljust(22, ' '),
              'PRECO DE FABRIDA'.ljust(22, ' '),
              'VENDAS'.ljust(22, ' '),
              'COMPRAS'.ljust(22, ' '),
              )
        for i in range(len(disponiveis)):
            i +=i
            print(str(disponiveis[i]).ljust(22, ' '),
                  str(preco_venda[i]).ljust(22, ' '),
                  str(qtd_disponivel[i]).ljust(22, ' '),
                  str(preco_fabrica[i]).ljust(22, ' '),
                  str(vendas[i]).ljust(22, ' '),
                  str(compras[i]).ljust(22, ' '),
                  )
    elif opcao == 2:
        disponiveis.append(str(input('Insira o nome do game : ')).upper())
        preco_venda.append(float(input('Insira o preco de venda do game : ')))
        qtd_disponivel.append(int(input('Insira a quantidade disponivel do game : ')))
        preco_fabrica.append(float(input('Insira o preco de fabrica do game : ')))
        vendas.append(0)
        compras.append(0)

    elif opcao == 1:
        item = str(input('Insira o nome do item que foi vendido : ').upper())
        indice = disponiveis.index(item)
        qtd_disponivel[indice] -= 1
        vendas[indice] += 1



