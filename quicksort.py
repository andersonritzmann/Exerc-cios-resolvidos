def particao(v,lo,hi):
    pivo = v[hi]
    i = lo
    for j in range(lo,hi):
        if v[j]<pivo:
            aux = v[j]
            v[j] = v[i]
            v[i] = aux
            i = i+1
    aux = v[i]
    v[i] = v[hi]
    v[hi] = aux
    return i

def quicksort(v,lo,hi):
    if lo<hi:
        p = particao(v,lo,hi)
        quicksort(v,lo,p-1)
        quicksort(v,p+1,hi)
    return v
        
lista =[1,0,4,2,5,2,3]
lista = quicksort(lista,0,len(lista)-1)
print(lista)
