def clean():
    print('\n' * 100)
clean()
while True:
    numeros = input('Digite o numero separado por espaço:')
    valores = [int(x) for x in numeros.split()]
    clean()
    if not numeros:
        print('A lista está vazia')
        continue
    else:
        maior_numero=max(valores)
        menor_numero=min(valores)
        diferenca=maior_numero-menor_numero
        print(f'A diferença entre o maior e o menor valor é:',diferenca,',O menor número da lista é:',menor_numero,',O maior número da lista é:',maior_numero)
        break
