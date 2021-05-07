def f(x):
  return float((x*x-2*x-4))
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
TOL = 0.001
if (f(a)*f(b) < 0):
  c = (a+b)/2
  while(abs(f(c))>TOL):
    if(f(a)*f(c) < 0):
      b = c
    else:
      a = c
    c = (a+b)/2
  print("A raiz da funcao: ", c)
  print("O valor da função é: ", f(c))
else:
  print ("Não há raízes no intervalo dado")
