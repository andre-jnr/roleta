import time
import random
# import keyboard

# Initial setup
balance = 100
numbers = [i for i in range(1, 6)]
allowed_rounds = 3
minimum_bet = 10

def clear_console():
  import os
  os.system('cls' if os.name == 'nt' else 'clear')

print('CASSINO DO JUNIN')
print('pressione ESC para sair do jogo')

try:
  while True:
    print(f'SALDO ATUAL: R${balance:.2f}')
    print(f'APOSTA MINIMA: R${minimum_bet:.2f}')
    bet = int(input(f'Valor da sua aposta: R$'))
    
    if bet < minimum_bet:
      clear_console()
      print(f'Tente novamente')
      continue

    if bet > balance:
      clear_console()
      print(f'você não saldo suficiente para essa aposta!')
      print('Tente novamente!')
      continue
    
except:
  ...