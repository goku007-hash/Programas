lista=[]
maior=0
menor=0
for contagem in range(0,3):
    lista.append(float(input(f'digite um valor para o posicionamento{contagem}:')))
    if contagem == 0:
        maior = menor = lista[contagem]
    else:
        if lista[contagem] > maior:
            maior = lista[contagem]
        if lista[contagem] > menor:
            menor = lista[contagem]
    print('='*30)
    print(f'numeros da lista: {lista}')
    print(f'maior numero da lista: {max(lista)}')
    for i,v in enumerate(lista):
        if min(lista)==v:
            print(f'{i}')
    print(f'menor numero da lista: {min(lista)}')
