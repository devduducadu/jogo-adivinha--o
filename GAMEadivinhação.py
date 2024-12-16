from random import randint
import time
computador =  randint(0, 10)

print(" oi sou seu computador vamos jogar. . . ")
time.sleep (2)
print(" acabei de pensar em um número entre 0 e 10. ")
time.sleep (2)
print(" será que você acerta? ")

chute = int(input(" qual o seu chute? "))
tentativas = 1

while not chute == computador:
    chute = int(input(" você falhou tente novamente "))
    tentativas += 1
print (f" parabens acertou, você precisou de {tentativas} tentativas para acertar ")

