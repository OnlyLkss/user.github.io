#Soma de todos os números de 1 até n usando for

n = int(input("Insira um número: "))

soma = 0

for i in range(0,n+1):
    if i%2==0:
        soma = soma+i
        #print(f'i = {i} e a soma da atual é {soma}')

print(f'\nA soma de todos os pares entre 1 e {n} é {soma}')

del(n, soma)

#Soma de todos os números de 1 até n usando while

n = int(input("Insira um número: "))

soma = 0

print(f'\nA soma de todos os pares entre 1 e {n} é ', end="")

while n>=0:
    if n%2==0:
        soma += n
    n -= 1

print(f'{soma}')

del(n, soma)