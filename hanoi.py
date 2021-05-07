
cont = 0
def transferir(n,origem,destino,auxiliar):
  global cont
  cont = cont+1
  
  if n==1 :
    destino = origem
    
  else :
    transferir(n-1, origem, auxiliar, destino)
    destino = origem
    transferir(n-1, auxiliar, destino, origem)
    

   

n = int(input("Digite o número de discos: "))
origem = 'A'
destino = 'B'
auxiliar = 'C'
transferir(n, origem, destino, auxiliar)
print("O número de iterações é dado por:",cont)
