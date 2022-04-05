'''
Nome: Matheus dos Anjos Martins         
Universidade: Universidade Federal do Vale do São Francisco - Univasf
Curso: Engenharia da Computação (dez/2022 com possibilidade de flexibilizar)
Semestre atual: 10º
'''

from operator import attrgetter

class Pacote:
    def __init__(self, codOrigem, codDestino, codLoggi, codVendedor,tipoProduto):
            self.origem = codOrigem
            self.destino = codDestino
            self.codLoggi = codLoggi
            self.vendedor = codVendedor
            self.tipoProduto = tipoProduto
            self.regiaoDestino = 'indefinida'
            self.regiaoOrigem = 'indefinida'
            self.validade = 'indefinida'
    
    def codigo(self):
        return 'Código: ' + self.origem + ' ' + self.destino + ' ' + self.codLoggi + ' ' + self.vendedor + ' ' + self.tipoProduto

    def __repr__(self):
        return 'Código: ' + self.origem + ' ' + self.destino + ' ' + self.codLoggi + ' ' + self.vendedor + ' ' + self.tipoProduto + '\nRegião de origem: Cidade '+ self.origem+ ', região ' + self.regiaoOrigem + '\nRegião de destino: Cidade '+ self.destino+ ', região ' + self.regiaoDestino +'\nCódigo Loggi: ' +self.codLoggi + '\nCódigo do vendedor do produto: ' + self.vendedor + '\n'

    

listaCodPacotes = ['288355555123888',
                '335333555584333',
                '223343555124001',
                '002111555874555',
                '111188555654777',
                '111333555123333',
                '432055555123888',
                '079333555584333',
                '155333555124001',
                '333188555584333',
                '555288555123001',
                '111388555123555',
                '288000555367333',
                '066311555874001',
                '110333555123555',
                '333488555584333',
                '455448555123001',
                '022388555123555',
                '432044555845333',
                '034311555874001']

#lista que conterá todos os pacotes
listaPacotes = []

for i in range(len(listaCodPacotes)):
   origem,destino,codLoggi,codVendedor,tipoProduto = listaCodPacotes[i][:3],listaCodPacotes[i][3:6],listaCodPacotes[i][6:9],listaCodPacotes[i][9:12],listaCodPacotes[i][12:]
   pacote = Pacote(origem,destino,codLoggi,codVendedor,tipoProduto)
   listaPacotes.append(pacote)
   #print(repr(listaPacotes[i]))

#1
print('\n1) Identificar a região de destino de cada pacote, com totalização de pacotes (soma região)\n')
#somas de cada região
somaNordeste = 0
somaSudeste = 0
somaSul = 0
somaCentroOeste = 0
somaNorte = 0

for i in range(len(listaPacotes)):
    if(listaPacotes[i].destino[:1]=='0'):
       listaPacotes[i].regiaoDestino = 'Sudeste'
       somaSudeste +=1
    elif(listaPacotes[i].destino[:1]=='1'):
        listaPacotes[i].regiaoDestino = 'Sul'
        somaSul+=1
    elif(listaPacotes[i].destino[:1]=='2'):
        listaPacotes[i].regiaoDestino = 'Centro-Oeste'
        somaCentroOeste+=1
    elif(listaPacotes[i].destino[:1]=='3'):
        listaPacotes[i].regiaoDestino = 'Nordeste'
        somaNordeste+=1
    elif(listaPacotes[i].destino[:1]=='4'):
        listaPacotes[i].regiaoDestino = 'Norte'
        somaNorte+=1
    print('A região de destino do pacote de ' + listaPacotes[i].codigo() + ' é a região ' + listaPacotes[i].regiaoDestino)

stringTotalPacotes ='Total de pacotes para o '
print(stringTotalPacotes + 'Sudeste: ' + str(somaSudeste))
print(stringTotalPacotes + 'Sul: ' + str(somaSul))
print(stringTotalPacotes + 'Centro-Oeste: ' + str(somaCentroOeste))
print(stringTotalPacotes + 'Nordeste: ' + str(somaNordeste))
print(stringTotalPacotes + 'Norte: ' + str(somaNorte))

#Identificando as regioes de origem
for i in range(len(listaPacotes)):
    if(listaPacotes[i].origem[:1]=='0'):
       listaPacotes[i].regiaoOrigem = 'Sudeste'
    elif(listaPacotes[i].origem[:1]=='1'):
        listaPacotes[i].regiaoOrigem = 'Sul'
    elif(listaPacotes[i].origem[:1]=='2'):
        listaPacotes[i].regiaoOrigem = 'Centro-Oeste'
    elif(listaPacotes[i].origem[:1]=='3'):
        listaPacotes[i].regiaoOrigem = 'Nordeste'
    elif(listaPacotes[i].origem[:1]=='4'):
        listaPacotes[i].regiaoOrigem = 'Norte'
    #print(listaPacotes[i].regiaoOrigem)

#2
print('\n2 Saber quais pacotes possuem códigos de barras válidos e/ou inválidos\n')
for i in range(len(listaPacotes)):
    if(listaPacotes[i].vendedor =='367' or (listaPacotes[i].regiaoOrigem == 'Centro-Oeste' and listaPacotes[i].tipoProduto == '001') or listaPacotes[i].tipoProduto not in ['001','111','333','555','888'] or listaPacotes[i].regiaoOrigem == 'indefinida'):
        listaPacotes[i].validade = 'Invalido'
    else:
        listaPacotes[i].validade = 'Valido'
    print('O ' + listaPacotes[i].codigo() + ' é ' + listaPacotes[i].validade)

# Salvando os pacotes válidos em uma lista
listaPacotesValidos = [listaPacotes[i] for i in range(len(listaPacotes)) if listaPacotes[i].validade =='Valido']

#3
print('\n3 Identificar os pacotes que têm como origem a região Sul e Brinquedos em seu conteúdo\n')
count = 0
for i in range(len(listaPacotesValidos)):
    if(listaPacotes[i].regiaoOrigem == 'Sul' and listaPacotes[i].tipoProduto == '888'):
        print(listaPacotes[i].regiaoOrigem + listaPacotes[i].tipoProduto)
        count+=1
if(not(count)):
    print('Nenhum pacote tem como origem a região Sul e Brinquedos em seu conteúdo ')

print('\n4 Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos)\n')
listaRegDestNordeste = []
listaRegDestNorte = []
listaRegDestSul = []
listaRegDestSudeste = []
listaRegDestCentroOeste = []

for i in range(len(listaPacotesValidos)):
        if(listaPacotesValidos[i].regiaoDestino=='Nordeste'):
            listaRegDestNordeste.append(listaPacotesValidos[i])
        elif(listaPacotesValidos[i].regiaoDestino=='Norte'):
            listaRegDestNorte.append(listaPacotesValidos[i])
        elif(listaPacotesValidos[i].regiaoDestino=='Sul'):
            listaRegDestSul.append(listaPacotesValidos[i])
        elif(listaPacotesValidos[i].regiaoDestino=='Sudeste'):
            listaRegDestSudeste.append(listaPacotesValidos[i])
        else:
            listaRegDestCentroOeste.append(listaPacotesValidos[i])
for i in range(len(listaRegDestNordeste)):
    print('A região de destino do pacote de ' + listaRegDestNordeste[i].codigo() + ' é a região ' + listaRegDestNordeste[i].regiaoDestino)

for i in range(len(listaRegDestNorte)):
    print('A região de destino do pacote de ' + listaRegDestNorte[i].codigo() + ' é a região ' + listaRegDestNorte[i].regiaoDestino)

for i in range(len(listaRegDestSudeste)):
    print('A região de destino do pacote de ' + listaRegDestSudeste[i].codigo() + ' é a região ' + listaRegDestSudeste[i].regiaoDestino)
    
for i in range(len(listaRegDestSul)):
    print('A região de destino do pacote de ' + listaRegDestSul[i].codigo() + ' é a região ' + listaRegDestSul[i].regiaoDestino)
    
for i in range(len(listaRegDestCentroOeste)):
    print('A região de destino do pacote de ' + listaRegDestCentroOeste[i].codigo() + ' é a região ' + listaRegDestCentroOeste[i].regiaoDestino)

#5
print('\n5 Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos)\n')
listaCodVendedorValidos = [listaPacotesValidos[i].vendedor for i in range(len(listaPacotesValidos))]
listaCodVendedorValidosUnicos = list(set(listaCodVendedorValidos))
for vendedor in listaCodVendedorValidosUnicos:
    print('O numero de pacotes enviados pelo vendedor '+ vendedor + ' foi '+ str(listaCodVendedorValidos.count(vendedor))) 

#6
print('\n6 Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos)\n')
for i in range(len(listaPacotesValidos)): 
       print('Código do pacote: '+ listaPacotesValidos[i].codigo() + ', Destino: '+ listaPacotesValidos[i].regiaoDestino +' e Tipo do produto: '+ listaPacotesValidos[i].tipoProduto)

#7
print('\n7 Se o transporte dos pacotes para o Norte passa pela Região Centro-Oeste, quais são os pacotes que devem ser despachados no mesmo caminhão?\n')
listapacotesCaminhaoNorteCentro = []
for i in range(len(listaPacotesValidos)):
    if(listaPacotesValidos[i].regiaoDestino=='Norte' or listaPacotesValidos[i].regiaoDestino=='Centro-Oeste'):
        listapacotesCaminhaoNorteCentro.append(listaPacotesValidos[i])
print('Codigos dos pacotes que devem ser despachados no mesmo caminhão:')
for i in range(len(listapacotesCaminhaoNorteCentro)):
    print(listapacotesCaminhaoNorteCentro[i].codigo())

#8 e 9
print('\n8 Se todos os pacotes fossem uma fila qual seria a ordem de carga para o Norte no caminhão para descarregar os pacotes da Região Centro Oeste primeiro; 9) No item acima considerar que as jóias fossem sempre as primeiras a serem descarregadas;\n')
listapacotesCaminhaoNorteCentroOrdenada = sorted(listapacotesCaminhaoNorteCentro,key=attrgetter('destino'))
print('A ordem de carga para o Norte no caminhão para descarregar os pacotes da Região Centro Oeste primeiro é: (considerando que uma fila tem como politica de acesso FIFO)')
for i in range(len(listapacotesCaminhaoNorteCentroOrdenada)):
    print(listapacotesCaminhaoNorteCentroOrdenada[i].codigo())

#10
print('\n10 Listar os pacotes inválidos.\n')
listaPacotesInvalidos = [listaPacotes[i] for i in range(len(listaPacotes)) if listaPacotes[i].validade =='Invalido']
print('Os pacotes invalidos possuem os seguintes códigos:')
for i in range(len(listaPacotesInvalidos)):
        print(listaPacotesInvalidos[i].codigo())