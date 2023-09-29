def clean():
    print('\n' * 100)
clean()
while True:
    lista_1=input('Digite 5 números para a lista 1(separado por espaço):')
    valores_lista_1=[int(x) for x in lista_1.split()]
    lista_2=input('Digite 5 números para a lista 2(separado por espaço):')
    valores_lista_2=[int(x) for x in lista_2.split()]
    clean()
    if not lista_1 and not lista_2:
        print('Alguma das listas estão vazia,digite novamente.')
        continue
    else:
        clean()
        lista_2,lista_1=lista_2,lista_1
        print('A lista 1 invertida é: ','[',lista_2,']')
        print('A lista 2 invertida é: ','[',lista_1,']')
        break