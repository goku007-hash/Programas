def clean():
      print('\n' * 10)
clean()
def soma(a,b):
        soma = a + b
        print('O resultado da soma é:',soma)
        return soma
def subtração(a,b):
        subtração = a - b
        print('O resultado da subtração é:',subtração)
        return subtração
def multiplicação(a,b):
        multiplicação = a * b
        print('O resultado da multiplicação é:',multiplicação)
        return multiplicação
def divisão(a,b):
        divisão = a / b
        print('O resultado da divisão é:',divisão)
        return divisão

vetor=[]
r=0
while True:
    print('Calculadora')
    print('1-Soma')
    print('2-Subtração')
    print('3-multiplicação')
    print('4-divisão')
    print('5-Sair')
    opcao=int(input('Qual operação você deseja realizar?'))
    
    clean()
    if opcao == 1 or opcao == 'soma':
            a = int(input('Digite o primeiro numero da soma:'))
            b = int(input('Digite o segundo numero da soma:'))
            clean()
            r=soma(a,b)
            vetor.append(r)
            continue
    elif opcao == 2 or opcao == 'subtração':
            a = int(input('Digite o primeiro numero da subtração:'))
            b = int(input('Digite o segundo numero da subtração:'))
            clean()
            r=subtração(a,b)
            vetor.append(r)
            continue
    elif opcao == 3 or opcao == 'multiplicação':
            a = int(input('Digite o primeiro numero da multiplicação:'))
            b = int(input('Digite o segundo numero da multiplicação:'))
            clean()
            r = multiplicação(a,b)
            vetor.append(r)
            continue
    elif opcao == 4 or opcao == 'divisão':
            a = int(input('Digite o primeiro numero da divisão:'))
            b = int(input('Digite o segundo numero da divisão:'))
            clean()
            r = divisão(a,b)
            vetor.append(r)
            continue
    elif opcao == 5 or opcao == 'Sair':
            clean()
            print('Calculadora encerrada.')
            
            break
    elif opcao < 1 or opcao > 5:
           print('Digite uma alternativa válida')
           continue
    

print(vetor)