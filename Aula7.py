Tarefa 2:
lista = [1,-8,3,-3,15]
i = 0
while i < len(lista):
    if lista[i] < 0:
        lista[i] = -lista[i]
    i+=1
print(lista)
---------------------------------------------------------
Tarefa 3:
lista = [1,-8,3,-3,15]
i = 0
while i < len(lista):
    if lista[i] < 0:
        lista.remove(lista[i])
    i+=1
print(lista)
-----------------------------------------------------------
Tarefa 4:
lista = []
soma = 0
while True:
    n = float(input("Nota: "))
    if n<0:
        print(f"A média das notas foi: {soma/len(lista)}")
        break
    lista.append(n)
    soma+=n
----------------------------------------------------------
Tarefa 5:
 listap = []
listai = []
while True:
    n = float(input("Numero: "))
    if n<0:
        print(f"Porcentagem de números pares: {len(listap)/(len(listap)+len(listai)) * 100} %\n")
        print(f"Porcentagem de números ímpares: {len(listai)/(len(listai)+len(listap)) * 100 } %")
        break
    elif n%2 == 0:
        listap.append(n)
    else:
        listai.append(n)
------------------------------------------------------------------------
Tarefa 6:
 lista = []
while True:
    n = int(input("Número: "))
    if n< 0:
        break
    elif n not in lista:
        lista.append(n)
print(f"Sua lista de números sem repetição é: {lista}")
--------------------------------------------------------------------------
Tarefa 7: *
    lista = []
i = 0

while i < 5:
    a = float(input("Altura: "))
    p = float(input("Peso: "))
    lista.append((a, p))

    tupla_igual = False
    for x in range(i):
            tupla_igual = True
            break

    if tupla_igual:
        print("Pelo menos duas pessoas têm a mesma altura e peso.")
        break

    i += 1

if not tupla_igual:
    print("Não há pessoas com peso e alturas iguais")
------------------------------------------------------------------------
Tarefa 8: ***
lista = []
i = 0
while i < 5:
    a = float(input("Altura: "))
    p = float(input("Peso: "))
    lista += [(a,p)]
    tupla_igual = False
    for x in range (len(lista)): 
        if  x in range(i):
            tupla_igual = True
            break
    i+=1
if tupla_igual == True:
    print("Pelo menos duas pessoas têm a mesma altura e peso.")
else:
    print("Não há pessoas com peso e alturas iguais")
-------------------------------------------------------------------------
Tarefa 9:
lista = [2,4,1,11,111, 5, 8, 9, 4]
new_lista = []
for x in lista:
    if x in [2, 5, 8, 9, 4]:
        new_lista.append(x)
print(f"Lista com números 2, 5, 8, 9, 4: {new_lista}")
-------------------------------------------------------------------------
Tarefa 10:
lista = [22,15,68,99,63]
qtd = 0
for e in lista:
    if e % 2 == 0:
        qtd+=1
print(qtd)
--------------------------------------------------------------------------
Tarefa 11:
nome = input("Nome: ")
soma = 0
vogal = "aeiouAEIOU"
for letra in nome:
    if letra in vogal:
        soma+=1
print(f"Seu nome possui {soma} vogais")
--------------------------------------------------------------------------
Tarefa 12:
for i in range(0,101):
    if i%2==0:
        print(i, end=' ')
 Exemplo 2:
list = [print(e, end =' ') for e in range(2,101,2) if True]
---------------------------------------------------------------------------
Livro automate the boring stuff
