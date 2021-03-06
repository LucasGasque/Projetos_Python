#Projeto-Controle de Estoques.
import os

def limpar(): #função para limpar a tela
    os.system("clear") 

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
    print('[7] Retirar produto cadastrado errado.')
    opção = input('Digite o numero da opção, ou \'encerrar\' para fechar o programa: ')
    limpar() #limpar a tela
  
    #Opções do terminal

    if opção == str(1): #Itens cadastrados.
        print('Produtos Cadastrados: ')
        for produto, preço in estoque_produtos.items():
            print(f'{produto.title()} R$: ' + str(preço))

    elif opção == str(2): #Quantidade de itens.
        print('Produtos em Estoque: ')
        for produto, quantidade in estoque_quantidades.items():
            print(f'{produto.title()}: ' + f'{str(quantidade)} unidades')

    elif opção == str(3): #Vendas
        print('Vendas: ')
        for produto, quantidade in vendas.items():
            print(f'{produto.title()}: ' + f'{str(quantidade)} unidades')

    elif opção == str(4): #Cadastrar produtos.
        produto = input('Digite o nome do produto cadastrado: ').lower()
        valor = float(input('Digite o preço: '))
        if produto in estoque_produtos:
            print('Já existe o produto', produto)
            alterar_valor = input('Alterar preço bolo("s/n"): ').lower()
            if alterar_valor == 's':
                estoque_produtos[produto] = valor             
        else:
            estoque_produtos[produto] = valor

    elif opção == str(5): #Registrar estoque.
        produto = input('Digite o nome do produto comprado: ')
        if produto in estoque_produtos: #verifica se o produto já foi cadastrado.
            quantidade = int(input('Digite a quantidade: ')) 
            if produto in estoque_quantidades: #verifica já existe o produto
                estoque_quantidades[produto] = int(estoque_quantidades[produto]) + quantidade #adiciona a quantidade registrada a já existente
            else:
                estoque_quantidades[produto] = quantidade #adiciona itens primeira x
        else:
            print('Produto não cadastrado!')

    elif opção == str(6): #Registrar vendas.
        produto = input('Digite o nome do produto a ser retirado: ')
        if produto not in estoque_quantidades:
            print('Produto não encontrado')
        else:
            quantidade = int(input('Digite a quantidade: '))
            if int(estoque_quantidades[produto]) < quantidade:
                print(f'Produtos insuficientes no estoque: {estoque_quantidades[produto]} restantes!')
            else:
                vendas[produto] = quantidade
                estoque_quantidades[produto] = int(estoque_quantidades[produto]) - quantidade

    elif opção == str(7): #Retirar itens cadastrados errados
        for produto, preço in estoque_produtos.items():
            print(f'{produto.title()} R$: ' + f'{preço}')
        produto = input('Qual item deseja remover?: ').lower()
        estoque_produtos.pop(produto)    

    else: #Encerrar o programa.
        if opção == 'encerrar':
            continue
        else: #caso opção não seja Nº ou encerrar.
            print('Opção invalida')
    
else: #encerramento do programa.
    print('Obrigado por usar o Terminal de estoque!')



