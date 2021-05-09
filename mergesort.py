def merge(esquerda,direita):
    resultado = []
    while len(esquerda)!=0 and len(direita)!=0:
        if esquerda[0] <= direita[0]:
            resultado.append(esquerda[0])
            del esquerda[0]
        else:
            resultado.append(direita[0])
            del direita[0]
    while len(esquerda)!=0:
        resultado.append(esquerda[0])
        del esquerda[0]
    while len(direita)!=0:
        resultado.append(direita[0])
        del direita[0]
    return resultado

def mergesort(m):
    if len(m) <= 1 :
        return m
    esquerda = []
    direita = []
    print(len(m))
    for i in range(0,len(m)):
        if i < (len(m)-1)/2 :
            esquerda.append(m[i])
        else:
            direita.append(m[i])
    esquerda = mergesort(esquerda)
    direita = mergesort(direita)
    
    return merge(esquerda,direita)
    
lista = [1,2,5,2,6,3,3]
lista = mergesort(lista)
print(lista)
