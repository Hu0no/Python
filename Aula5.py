22.
maior = -40000
x = 1
while x <= 5:
    n=int(input("Numero: "))
    if n > maior:
        maior = n
    x+=1
print(f'O maior número é {maior}')
--------------------------------------------------------------------
23.
maior = 0
x = 1
while x <= 5:
    n=float(input("Nota: "))
    if n < 0 or n > 10:
        print('nota inválida')
        break
    elif n > maior:
        maior = n
    x+=1
if n>0 and n <= 10:
    print(f'A maior nota é {maior}')
-------------------------------------------------------------------
27.
i = 1
while i<=10:
    print(f'Tabuada de {i}: ')
    j=1
    while j<= 10:
        print(f'{i} x {j} = {i*j}')
        j+=1
    i+=1
--------------------------------------------------------------------
28.
while True:
    i = 1
    n = int(input("Numero: "))
    if n<0:
        break
    cont = 0
    while i<=n:
        if n%i==0:
            cont+=1
        i+=1
    print(f'{n} tem {cont} divisores')
-----------------------------------------------------------------------
1.
palavra = ""
while True:
    letra = input("Letra: ")
    palavra += letra
    if letra == " ":
        break

print(f"Palavra formada: {palavra}")
------------------------------------------------------------------------
1.
p = input("Palavra: ")
print(f'A palavra digitada tem {len(p)} letras')
------------------------------------------------------------------------
2.
p = input("Palavra: ")
np = p.upper()
print(np)
-------------------------------------------------------------------------
3.
p = input("Palavra: ")
np = p.lower()
print(np)
-------------------------------------------------------------------------
