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
