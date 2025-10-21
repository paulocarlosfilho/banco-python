#Dobro
def dobro(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in dobro(numeros=[50, 100]): 
    print(i)