while True:
    numeros = input('Digite o numero separado por espaço:')
    valores = [int(x) for x in numeros.split()]
    if not numeros:
        print('A lista está vazia')
        continue
    else:
        maior_numero=max(valores)
        menor_numero=min(valores)
        diferenca=maior_numero-menor_numero
        print('A diferença entre o maior e o menor valor é:',diferenca)
        break