lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')


# TUPLAS CRUA COM ('','')
# print(lanche)

# TUPLAS ORGANIZADAS EM ORDEM ALFABETICA
# print(sorted(lanche))

# APENAS NOMES DAS TUPLAS
# for c in (lanche):
#     print(c)


# APENAS NOME DA TUPLA2
# for comida in (lanche):
#     comida = lanche[2]
# PARA TODOS EXCLUIR LINHA ACIMA
# print(f'Eu comi {comida}')

# POSIÇÃO MOSTRA A LETRA DO INDICE 2 DE CONT(2º ITEM DA LISTA)
# cont = lanche[2]
# print(f'Eu comi {cont} na posição {cont[2]}')


# APENAS CONTAR QUANTOS TEM NA TUPLA
# print(len(lanche))


# INDICE DAS TUPLAS(posiçõesN)
# for cont in range(0, len(lanche)):
#     print(cont)

# # TODAS TUPLAS SEM POSIÇÃO
# for contador in lanche:
#     print(f'Eu comi {contador}')
# # OU MAIS CHATO DE LER
# for contador in range(0, len(lanche)):
#     print(f'Eu comi {lanche[contador]}')

# TODAS TUPLAS COM POSIÇÕES
# for pos, comida in enumerate(lanche):
#     print(f'Eu comi {comida} que esta na posição {pos}')
# OU
# for comida in range(0, len(lanche)):
#     print(f'Eu comi {lanche[comida]} que esta na posição {comida}')


# TUPLA()
# LISTA[]
# DICIONARIO{}
# print(len(lanche))
# print(lanche[0::3])


# # Criando a primeira tupla com números
# tupla1 = tuple(i for i in range(10))

# # Criando a segunda tupla com palavras
# tupla2 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
#           'seis', 'sete', 'oito', 'nove', 'dez')

# # Atribuindo o valor do segundo item da tupla2 ao primeiro item da tupla1
# tupla1 = (tupla2[1],) + tupla1[1:]

# # Imprimindo as tuplas combinadas
# for i in range(10):
#     print(tupla1[i], tupla2[i])
