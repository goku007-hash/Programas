def clean():
    print('\n' * 100)
clean()
while True:
    lista_1=input('Digite os valores da lista 1(Separado por espaços!):')
    valores_lista_1=[int(x)for x in lista_1.split()]
    lista_2=input('Digite os valores da lista 2(Separado por espaços!):')
    valores_lista_2=[int(x) for x in lista_2.split()]
    pares_lista1=0
    pares_lista2=0
    clean()
    if not lista_1 and not lista_2:
        print('Digite os números nas duas listas!')
        continue
    for valores_lista_1 in valores_lista_1:
        if valores_lista_1 % 2 == 0:
            pares_lista1 += valores_lista_1
            clean()
    for valores_lista_2 in valores_lista_2:
        if valores_lista_2 % 2 == 0:
            pares_lista2 += valores_lista_2
            clean() 
        print(pares_lista1+pares_lista2)
    break