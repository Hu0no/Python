Tarefa 30:
primos = 0
n = int(input("Digite n: "))
while n > 0:
    i = 1
    qtd_divisores = 0
    while i <= n:
        if n % i == 0:
            qtd_divisores += 1
        i += 1
    if qtd_divisores == 2:
        primos += 1
    n = int(input("Digite n: "))
print(f'Quantidade de primos: {primos}')
-----------------------------------------------------------------------------------------------------
Tarefa 29:***
  n = int(input("Digite n: \n"))
while n>0:
    i = 1
    qtd_divisores = 0
    while i <= n:
        if n % i == 0:
        qtd_divisores += 1
        if qtd_divisores == 2:
        print(f"{n} é primo")
        else:
        print(f"{n} não é primo")
        i += 1
    n = int(input("Digite n: \n"))
------------------------------------------------------------------------------------------------------
Função list:
x = list("abc")
print(x)
--------------------------------------------------------------------------------------------------------
Tarefa 1:
lista = []
i = 1
while i <= 5:
    n = int(input("Digite n: "))
    lista.append(n)
    i+=1 

print(f"{lista}")
-------------------------------------------------------------------------------------------------------------
