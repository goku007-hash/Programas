def criptografado(mensagem, deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    trans = str.maketrans(alfabeto, alfabeto[deslocamento:] + alfabeto[:deslocamento])
    return mensagem.translate(trans)
mensagem_usuario=input('Digite sua mensagem(Com letra minuscula): ')
deslocamento=int(input('em quantas posição você quer deslocar sua mensagem? '))
criptografia = criptografado(mensagem_usuario,deslocamento)
print('Mensagem criptografada:',criptografia)