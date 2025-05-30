def quicksort(lista, inicio, fim):

    if inicio < fim:
        posicao_pivo = particao(lista, inicio, fim)

        quicksort(lista, inicio, posicao_pivo - 1)

        quicksort(lista, posicao_pivo + 1, fim)

def particao(lista, inicio, fim):

    pivo = lista[fim] 
    i = inicio - 1    

    for j in range(inicio, fim):

        if lista[j] <= pivo:
            i += 1 
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]

    return i + 1
