import random
#Funcao que cria uma lista de X numeros aleatórios sem repeti-los e em ordem crescente
def randomLista(qtd):
    cont = 0
    lista = []    
    while cont < qtd:
        sorteado = random.randint(1,100)       
        while sorteado in lista:
            sorteado = random.randint(1,100) 
        else:
            lista.append(sorteado)
        cont += 1
    return lista

listaDes = randomLista(75)
print(listaDes)
def achaMaior(lista):
    maiorIndex = 0
    maior = lista[maiorIndex]

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            maiorIndex = i
    return maiorIndex


def selectionSort(listaDesordenada):
    listaOrdenada = []
    for i in range(0, len(listaDesordenada)):
        maior = achaMaior(listaDesordenada)
        listaOrdenada.append(listaDesordenada.pop(maior))
    return listaOrdenada

print(selectionSort(listaDes))

