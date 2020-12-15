#Projeto-Controle de Estoques.

#variaveis.
estoque_produtos = {} #Produto.item : valor.value.
estoque_quantidades = {} #Produto.item : quantidade.value.
vendas = {} #Produtos vendidos
opção = str((''))

# Terminal
while opção != 'encerrar': #loop para usar as funções multiplas vezes.
    print('-' * 100)
    print(' ' * 40, 'Terminal Estoque', ' ' * 40)
    print('-' * 100)
    print('[1] Vizualizar itens cadastrados.')
    print('[2] vizualizar quantidade de itens no estoque.')
    print('[3] Vizualizar vendas.')
    print('[4] Cadastrar novo item no estoque.')
    print('[5] Cadastrar compra de itens.')
    print('[6] Cadastrar retirada de itens.')
    opção = input('Digite o numero da opção, ou \'encerrar\' para fechar o programa: ')

    #Opções do terminal

    if opção == str(1): #Itens cadastrados.
        for produto, preço in estoque_produtos.items():
            print(f'{produto.title()} R$: ' + str(preço))

    elif opção == str(2): #Quantidade de itens.
        for produto, quantidade in estoque_quantidades.items():
            print(f'{produto}: ' + f'{str(quantidade)} unidades')

    elif opção == str(3): #Vendas
        for produto, quantidade in vendas.items():
            print(f'{produto} R$: ' + str(quantidade))

    elif opção == str(4): #Cadastrar produtos.
        produto = input('Digite o nome do produto cadastrado: ').lower()
        valor = float(input('Digite o preço: '))
        if estoque_produtos.get(produto):
            print('Já existe o produto', produto)
        else:
            estoque_produtos[produto] = valor

    elif opção == str(5): #Registrar estoque.
        produto = input('Digite o nome do produto comprado: ')
        if produto in estoque_produtos: #verifica se o produto já foi cadastrado.
            quantidade = int(input('Digite a quantidade: '))
            if estoque_quantidades.get(produto):
                print('Já existe o produto', produto)
            else:
                estoque_quantidades[produto] = quantidade
        else:
            print('Produto não cadastrado!')

    elif opção == str(6): #Registrar vendas.
        produto = input('Digite o nome do produto a ser retirado: ')
        if produto not in estoque_quantidades:
            print('Produto não encontrado')
        else:
            quantidade = int(input('Digite a quantidade: '))
            vendas[produto] = quantidade

    else: #Encerrar o programa.
        if opção == 'encerrar':
            continue
        else: #caso opção não seja Nº ou encerrar.
            print('Opção invalida')

else: #encerramento do programa.
    print('Obrigado por usar o Terminal de estoque!')



