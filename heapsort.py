def peneira(v,inicio,fim):
    raiz = inicio
    while (2*raiz+1)<=fim:
        filho = 2*raiz+1
        troca = raiz
        if v[troca]<v[filho]:
            troca = filho
        if (filho+1)<=fim and v[troca]<v[filho+1]:
            troca = filho+1
        if troca == raiz:
            return 0
        else:
            aux = v[raiz]
            v[raiz] = v[troca]
            v[troca] = aux
            raiz = troca

def heap(v):
    inicio = int((len(v)-2)/2)
    while inicio>=0:
        peneira(v,inicio,len(v)-1)
        inicio = inicio-1

def heapsort(v):
    heap(v)
    fim = len(v)-1
    while fim>0:
        aux = v[fim]
        v[fim] = v[0]
        v[0] = aux
        fim = fim-1
        peneira(v,0,fim)
    return v
        
lista =[1,0,4,2,5,2,3]
lista = heapsort(lista)
print(lista)
