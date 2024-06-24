import random


print("=" * 50)
print("Seja bem vindo ao jogo de adivinhação de números")
print("Acerte o número entre 1 e 100 para vencer")
print("=" * 50)


print("\nPara começar, selecione a dificuldade do jogo")
print("Lembre-se de que: A dificuldade da o número de chances")
escolha = input("\n(F) FÁCIL  -   (M) MÉDIO   -   (D) DIFÍCIL   ===  Escolha: ").lower()



if escolha      == 'f':
    chances = 20
elif escolha    == 'm':
    chances = 10
elif escolha    == 'd':
    chances = 5
else:
    print('Erro! Selecione uma opção de dificuldade válida')
    
print(f'Você terá {chances} chances para acertar. Boa sorte!')



numero = random.randint(1, 100)
count  = 1


while count <= chances:
    print('')
    print("-" * 50)
    print(f'Rodada: {count}')
    print("-" * 50)
    chute = input('Digite seu chute: ')
    
    try:
        chute_int   = int(chute)
    except:
        print('Digite um número válido')
        continue
    
    
    if chute_int    == numero:
        print('Parabéns!! Você acertou.')
        break
    
    
    if chute_int  <= numero:
        print('Chute abaixo do número correto')
    else:
        print('Chute acima do número correto')
    
    
    if count == chances:
        print('Você perdeu!')
        break
    
    count +=1
        
        