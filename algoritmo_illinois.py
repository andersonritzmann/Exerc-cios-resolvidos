def funcao(x):
    return float(2*x*x*x - 4*x*x + 3*x)
x0 = float(input("Digite a aproximação para x0: "))
x1 = float(input("Digite a aproximação para x1: "))
iteracoes = 100
i = 2
f0 = funcao(x0)
f1 = funcao(x1)
TOL = 0.001
convergiu = False
while i<=iteracoes:
    x = (f1*x0 - 0.5*f0*x1)/(f1-0.5*f0)
    if abs(x-x1)<TOL:
        print(x)
        convergiu = True
    i = i+1
    f = funcao(x)
    if f*f1 < 0:
        x0=x1
        f0=f1
    x1=x
    f1=f
if not convergiu:
    print("Deu errado")
