from cartas import Carta
from jogo import comparar

# Criando cartas de exemplo
carta1 = Carta("Dragão", {"força": 90, "velocidade": 60, "inteligência": 70})
carta2 = Carta("Fênix", {"força": 85, "velocidade": 80, "inteligência": 65})

print("Bem-vindo ao Super Trunfo (versão simples)!\n")
print("Cartas disponíveis:")
print(carta1)
print(carta2)

# Jogador escolhe atributo
atributo = input("\nEscolha um atributo (força, velocidade, inteligência): ").lower()
resultado = comparar(carta1, carta2, atributo)
print("\nResultado:", resultado)
