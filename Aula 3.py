Tarefa 1:
  n = int(input("Insira um número: "))
if n >= 0:
    print(n)
elif n < 0:
    print(-n)

---------------------------------------------------------
Tarefa 2:
  a = int(input("Início do intervalo: "))
b = int(input("Fim do intervalo: "))
if b < a:
    temp = a
    a = b
    b = temp
print(f'Intervalo : [{a},{b}]')
------------------------------------------------------------
Tarefa 3:
  a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
soma = -b/a
produto = c/a
print("Soma: ", soma, "Produto: ", produto)
--------------------------------------------
Tarefa 4:
  v = int(input("velocidade: "))
if v > 80:
    print("Você foi multado")
    multa = (v - 80) * 5
    print("Valor da multa: R$ ", multa)
else:
    print("Você está dentro do limite de velocidade permitido")
    ------------------------------------------------
    Tarefa 5:
      num = int(input("Insira um número: "))
if num % 2 == 0:
    print("Seu número é par")
else:
    print("Seu número é ímpar")
    -------------------------------------------------------
    Tarefa 6:
      N = 3
M = 5
if N - M > 0:
    M = N - M
else:
    N = M - N
print(N, M)
------------------------------------------------------------
Tarefa 7:
  N = 4
if N%2 ==0:
    M = N * 2
else:
    N = N + 1
    M = M * 2
print(N, M)
----------------------------------------------------------------
Tarefa 8:
  n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
if (n1+n2)/2 >=7:
    print("Aprovado")
else:
    print("Reprovado")
    -------------------------------------------------------------
    Tarefa 9:
      n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
e = float(input("Nota exame: "))
if (n1 + n2)/2 >= 7:
    print("Média final: ", (n1 + n2)/2 )
else:
    print("Média final: ", n1*0.3 + n2 * 0.3 + e * 0.4)
    ----------------------------------------------------------------
    Tarefa 10:
      t = int(input("Tempo: "))
if t <= 15:
    print("Grátis")
elif t < 60:
    print("R$ 3.00")
else:
    print("R$ 6.00")
-------------------------------------------------------------------
Tarefa 11:
  d = int(input("Distância: "))
if d <= 200:
    print("Custo: R$ ", 0.5 * d )
elif d < 400:
    print("Custo: R$ ", 0.45 * d)
else:
    print("Custo: R$ ", 0.4 * d)
  
