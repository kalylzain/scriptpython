print('Calculando a area a ser coberta ou forrada')
print('Digite os valores solicitados em M2 e no lugar de virgula use ponto')
comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))
area = comprimento * largura
print('A area total é de: ', area,'M2')
material = input('Digite o material usado para cobrir a area: ')
unidade = input('Qual a unidade de medida do material: ')
compmat = float(input('Qual o comprimento do material: '))
largmat = float(input('Qual a largura do material: '))
areamat = compmat * largmat
print('O tamanho da area do material é de: ',areamat, 'Cm' )


