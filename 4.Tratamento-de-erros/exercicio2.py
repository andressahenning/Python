#ATIVIDADE: Desenvolva um programa que só deve aceitar números pares. 

while True:
    try:
        n1 = int(input('Informe um número par: '))

        if n1 % 2 == 0:
            print(f'Parabéns! Você digitou um número PAR! {n1}')
            break
        else:
            print('Você digitou um número ímpar! Tente novamente.')

    
    except(ValueError, TypeError):
        print('[ERRO] Caractere inválido! Tente novamente.')
    
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os dados!')
    