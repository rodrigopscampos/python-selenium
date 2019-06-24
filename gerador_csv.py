colunas = []

while True:
    c = input('Coluna ou Enter para continuar: ')
    if c == "": break
    colunas.append(c)

if len(colunas) == 0:
    pass

qtd_linhas = int(input('Quantidade de linhas: '))
linhas = []
for i in range(1, qtd_linhas + 1):
    print('Linha ' + str(i))
    linha = []
    for c in colunas:
        linha.append(input(c + ': '))
    linhas.append(linha)

endereco_arquivo = input('Endereço do arquivo: ')

if not endereco_arquivo.endswith('.csv'):
    endereco_arquivo = endereco_arquivo + '.csv'

print('Arquivo: ' + endereco_arquivo)

f = open(endereco_arquivo, 'w')

f.write( ";".join(colunas) + '\n' )

for l in linhas:
    f.write(";".join(l) + '\n')

f.close()

print('Pressione Enter para ler o arquivo')

f = open(endereco_arquivo, 'r')

for l in f:
    print(l, end="")