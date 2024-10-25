import random

# Gera um número secreto aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Número máximo de tentativas
tentativas_maximas = 3

# Contador de tentativas
tentativas = 0

print("Bem-vindo ao Jogo de Adivinhação!")
print("Você tem até 3 tentativas para adivinhar o número correto (entre 1 e 10).")

# Loop para permitir múltiplas tentativas
while tentativas < tentativas_maximas:
    # Solicita que o jogador faça uma tentativa
    palpite = int(input("Digite seu palpite (entre 1 e 10): "))
    
    # Incrementa o número de tentativas
    tentativas += 1
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print(f"Tentativa {tentativas} incorreta. Tente novamente!")
        
# Verifica se todas as tentativas foram usadas sem sucesso
else:
    print("Que pena! Você esgotou suas 3 tentativas.")
    print(f"O número correto era {numero_secreto}. Melhor sorte na próxima vez!")
