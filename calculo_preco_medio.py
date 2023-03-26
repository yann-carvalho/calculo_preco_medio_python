# Aplicação para cálculo de preço médio de ativos de renda variável


ticker = input('Insira o ticker da ação adquirida: ')

data1 = input('Informe a data de compra (Ex.: 01/01/2023): ')
qtde = int(input(f'Insira a quantidade de ações compradas na data {data1}: '))
preco = float(input('Insira o preço de compra: '))

data2 = input('Informe nova data de compra (Ex.: 01/01/2023): ')
qtde2 = int(input(f'Insira a quantidade de ações compradas na data {data2}: '))
preco2 = float(input('Insira o preço de compra: '))

data3 = input('Informe nova data de compra (Ex.: 01/01/2023): ')
qtde3 = int(input(f'Insira a quantidade de ações compradas na data {data3}: '))
preco3 = float(input('Insira o preço de compra: '))

precom = (((qtde * preco) + (qtde2 * preco2) + (qtde3 * preco3)) / (qtde + qtde2 + qtde3))
print(f'O seu preço médio de {ticker} é R$ {precom:.2f}')