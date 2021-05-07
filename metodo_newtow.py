def f(x):
  return float((x*x-2*x-4))
def fx(x):
  return float((2*x-2))
k=1
n = int(input("Digite o número de iterações desejadas: "))
TOL = 0.001
convergiu = False
p0 = float(input("Digite um valor inteiro como chute inicial: "))
while (k<=n):
  p = (float)(p0- f(p0)/fx(p0))
  if(abs(p-p0)<TOL):
    print ("A solução final é: ")
    print(p)
    k=n+1
    convergiu = True
  p0 = p
  k = k+1
if(not convergiu):
  print("O método falhou")
