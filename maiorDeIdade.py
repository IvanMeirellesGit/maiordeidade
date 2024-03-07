def verificar_maioridade(idad):
    if idad < 0 or idad > 130:
        print('Por favor, digite uma idade válida.')
    elif idad < 18:
        print('Você é menor de idade!')
    elif 18 <= idad < 65:
        print('Você já é adulto!')
    else:
        print('Você está na melhor idade.')


print('Bem-vindo ao meu programa de verificação de maioridade.')

while True:  # loop para idade valida
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Por favor, digite um número válido para idade.')
        continue  # reseta o loop

    verificar_maioridade(idade)

    estado = input('Você deseja executar novamente? (S/N):')
    if estado.upper() != 'S':
        print('Até mais!')
        break
