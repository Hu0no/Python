Tarefa 1:
i = 1
while i < 11:
    print(i)
    i+=1
------------------------------------------------------------------------------------
    Tarefa 2:
      n = 2
while n <= 100:
    print(n)
    n += 2
-------------------------------------------------------------------------------------
Tarefa 3:
  n = 10
while n >=0:
    print(n)
    n-=1
--------------------------------------------------------------------------------------
Tarefa 4:
  n = int(input("Numero: "))
x = 1
while x <=10:
    result = x*n
    print(result)
    x+=1
---------------------------------------------------------------------------------------
Tarefa 5:
  n = int(input("Numero: "))
x = n
while n != 0:
    print(x)
    n = int(input("Numero: "))
---------------------------------------------------------------------------------------
Tarefa 6:
  n = int(input("Numero: "))
while n != 0:
    if n%2 == 0:
        print("Par")
    else:
        print("Ímpar")
    n = int(input("Numero: "))
---------------------------------------------------------------------------------------
Tarefa 7:
x = 1
while x <=5:
    n = int(input("Número: "))
    if n < 0:
        print("Negativo")
    elif n > 0:
        print("Positivo")
    x+=1
----------------------------------------------------------------------------------------
Tarefa 8:
--------------------------------------------------------------------------------------
Tarefa 9:
---------------------------------------------------------------------------------------
Tarefa 10: 
  x = 1
soma = 0
while x < 100:
    soma+=x
    x+=1
print(soma)
--------------------------------------------------------------------------------------------
Tarefa 11:
 x = 1
soma = 0
while x <= 10:
    n = int(input("Número: "))
    soma += n
    x+=1
print(f'Soma: {soma}')
---------------------------------------------------------------------------------------------
Tarefa 12:
  x = 0
soma = 0
while x < 1000:
     soma += x
     x+=5
print(f"Soma: {soma}")
-----------------------------------------------------------------------------------------------
Tarefa 13:
  soma = 0
while soma <= 1000:
    n = int(input("Num: "))
    soma += n
print(f"Soma : {soma}")
-----------------------------------------------------------------------------------------------
Tarefa 14:
 soma = 0
tamanho = 1
while tamanho <= 50:
    n = int(input("Numero: "))
    soma += n
    media = soma/tamanho
    tamanho += 1
    print(f"A média é {media}")
-----------------------------------------------------------------------------------------------
Tarefa 15:
  soma = 0
while True:
    n = int(input('num: '))
    if n < 0:
        break
    soma += n
print(f'Soma: {soma}')
-----------------------------------------------------------------------------------------------
Tarefa 16:
    soma = 0
while True:
    n = int(input("Numero: "))
    if n < 0 and n%2 == 0:
        soma += n
        print(f"Soma: {soma}")
        break
    elif n < 0 and n%2 != 0:
        print(f"Soma: {soma}")
        break
    elif n > 0 and n%2 == 0:
        soma += n
----------------------------------------------------------------------------------------------
Tarefa 17:
  t = 1
s = 0
while t<=10:
    n = int(input("Num: "))
    if n<0:
        s+=1
    t+=1
print(f"{s}  números negativos.")
-------------------------------------------------------------------------------------------------
Tarefa 18:
  n = int(input("Num: "))
x = n
count = 0
while x>0:
    if n%x == 0:
        count += 1
    x-=1
print(count)
--------------------------------------------------------------------------------------------------
Tarefa 19:
    count = 0
while True:
    n = int(input("Numero: "))
    if n < 0 and n%2 == 0:
        count += 1
        print(f"Quantidade de números pares: {count}")
        break
    elif n < 0 and n%2 != 0:
        print(f"Quantidade de números pares: {count}")
        break
    elif n > 0 and n%2 == 0:
        count += 1
 --------------------------------------------------------------------------------------------------
Tarefa 20:
    count = 0
tamanho = 0
while True:
    n = int(input("Numero: "))
    if n < 0:
        result = (count / tamanho)*100
        print(f"Porcentagem de números pares: {result:.2f}%")
        break
    elif n%2 == 0:
        count += 1
        tamanho +=1
    else:
        tamanho += 1
--------------------------------------------------------------------------------------------------
Tarefa 21:
    soma = 0
tamanho = 0
while True:
    n = int(input("Numero: "))
    if n < 0:
        media = soma/tamanho
        print(f"A média dos números pares é: {media}")
        break
    elif n%2 == 0:
        soma += n
        tamanho +=1
