import time
import keyboard

# Initial setup
balance = 100
numbers = [i for i in range(1, 6)]
repetitions = 3
minimum_bet = 10

def clear_console():
  import os
  os.system('cls' if os.name == 'nt' else 'clear')


def choose_random_number():
  import random
  return random.choice(numbers)


def negative_balance(balance):
  if balance <= 0:
    print('Você ficou sem saldo! O jogo acabou')
    return True

def start_roulette():
  print('GIRANDO ROLETA')
  for _ in range(repetitions):
    for i in numbers:
      if keyboard.is_pressed('esc'):
        print('jogo encerrado!')
        print('obrigado por jogar!')
        exit()
      print(f'\r{i}', end='', flush=True)
      time.sleep(0.2)
  
  drawn_number = choose_random_number()
  print(f'\nO número sorteado foi {drawn_number}')

  if drawn_number == 3:
    winnings = bet * 5
    balance += winnings
    print(f'Parabéns, você ganhou R${winnings}!')

  else:
    balance -= bet
    print(f'Que pena! Você perdeu R${bet}.')

print('CASSINO DO JUNIN')
print('pressione ESC para sair do jogo')

try:
  while True:
    print(f'SALDO ATUAL: R${balance:.2f}')
    print(f'APOSTA MINIMA: R${minimum_bet:.2f}')
    bet = int(input(f'Valor da sua aposta: R$'))

    if keyboard.is_pressed('esc'):
        print('jogo encerrado!')
        print('obrigado por jogar!')
        exit()
    
    if bet < minimum_bet:
      clear_console()
      print(f'Tente novamente')
      continue

    if bet > balance:
      clear_console()
      print(f'você não saldo suficiente para essa aposta!')
      print('Tente novamente!')
      continue

    start_roulette()

    if negative_balance(balance):
      break

except Exception as e:
  print(f'Erro no jogo: {e}')