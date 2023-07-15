# Function padrão para definição de valores em armas
def weapon(i, f, hit_i, hit_f, arma):
  import random
  forca_generator = random.randint(i, f)
  forca = forca_generator
  if arma == 'espada' or arma == 'adaga':
    tratamento = 'Sua'
  else:
    tratamento = 'Seu'
  print(f'{tratamento} {arma} esta no Lvl. 1 e possui uma margem de dano de {i}-{forca}')
  print()
  global ini
  global hit_ini
  global hit_fim
  global strength
  ini = i
  hit_ini = hit_i
  hit_fim = hit_f
  strength = forca
  return ini, hit_ini, hit_fim, strength

# Function padrao para avanco entre etapas do jogo
def avancar():
  avanco = input('Aperte enter para avancar 1 passo.')
  print()
  while avanco != '':
    avanco = input('Aperte enter para avancar 1 passo.')
    print()

# Function que simula uma espécie de dice roll(utilizado com diversos propósitos em RPGs)
def roll():
  import random
  min = 1
  max = 10
  global roll_result
  roll_result = random.randint(min, max)
  return roll_result

# Function padrao para encontros com monstros
def monster_encounter(monster, monster_life, monster_strength_ini, monster_strength_fim):
  print(f'Voce encontrou {monster}.')
  global vida
  while monster_life > 0 and vida > 0:
    import random
    vida += 3
    print('--------------------------------------------------')
    acao = input('Escolha uma acao a tomar: ataque, defesa, fuga: ').lower()
    print('--------------------------------------------------')
    while acao != 'ataque' and acao != 'defesa' and acao != 'fuga':
      print('Por favor, escolha uma acao valida.')
      print()
      acao = input('Escolha uma acao a tomar: ataque, defesa, fuga: ').lower()
      print()
    if acao == 'ataque':
      chance = random.randint(hit_ini, hit_fim)
      attack = random.randint(ini, strength)
      monster_attack = random.randint(monster_strength_ini, monster_strength_fim)
      if chance >= 100:
        print(f'Voce ocasionou {attack}DMG em {monster}.')
        print()
        print(f'{monster} ocasionou {monster_attack}DMG aos seus pontos de vida.')
        print()
        monster_life -= attack
        vida -= monster_attack
        if monster_life > 0:
          print(f'{monster} tem agora {monster_life} pontos de vida restantes.')
          print()
        elif monster_life <= 0:
          print(f'{monster} esta morto(a).')
          print()
        if vida > 0:
          print(f'Voce tem agora {vida} pontos de vida restantes.')
          print()
        elif vida <= 0:
          print('Voce esta morto(a).')
      else:
        print('Voce errou o ataque.')
        print()
        monster_attack = random.randint(monster_strength_ini, monster_strength_fim)
        print(f'{monster} ocasionou {monster_attack}DMG aos seus pontos de vida.')
        print()
        vida -= monster_attack
        if vida > 0:
          print(f'Voce tem agora {vida} pontos de vida restantes.')
          print()
        elif vida <= 0:
          print('Voce esta morto.')
    elif acao == 'defesa':
      defense_chance_true = 0
      defense_chance_false = 1
      defesa = random.randint(defense_chance_true, 
      defense_chance_false)
      if defesa == 0:
        print('Sucesso! Voce defendeu o ataque.')
      elif defesa == 1:
        print('A defesa falhou.')
        print()
        monster_attack = random.randint(monster_strength_ini, monster_strength_fim)
        print(f'{monster} ocasionou {monster_attack}DMG aos seus pontos de vida.')
        print()
        vida -= monster_attack
        if vida > 0:
          print(f'Voce tem agora {vida} pontos de vida restantes.')
          print()
        elif vida <= 0:
          print('Voce esta morto.')
    elif acao == 'fuga':
      flee_chance_true = 0
      flee_chance_false = 1
      fuga = random.randint(flee_chance_true, 
      flee_chance_false)
      if fuga == 0:
        monster_life = 0
        print('Voce fugiu!')
        print()
      elif fuga == 1:
        print('Voce nao conseguiu fugir da batalha.')
        print()
        monster_attack = random.randint(monster_strength_ini, monster_strength_fim)
        print(f'{monster} ocasionou {monster_attack}DMG aos seus pontos de vida.')
        print()
        vida -= monster_attack
        if vida > 0:
          print(f'Voce tem agora {vida} pontos de vida restantes.')
          print()
        elif vida <= 0:
          print('Voce esta morto.')
  return vida

# Ganho de ouro encontrado pelo caminho
def gold_gain(gold, quantidade_moedas):
  print(f'Voce encontrou um pote de ouro contendo {quantidade_moedas}g !')
  global ouro
  ouro += quantidade_moedas
  return ouro

print('Bem-vindo(a) ao Glorious Journey, sua jornada gloriosa(dependendo de suas escolhas) comeca agora.')
print()

# Atribui o valor à variável arma
arma = input('Por favor, escolha sua arma inicial: espada, machado, adaga, arco ou sabre magico: ').lower()
print()

# Sistema anti-erros na escolha das armas
while arma != 'espada' and arma != 'machado' and arma != 'adaga' and arma != 'arco' and arma != 'sabre magico':
  print('Por favor, escolha uma opcao valida.')
  print()
  arma = input('Por favor, escolha sua arma inicial: espada, machado, adaga, arco ou sabre magico: ').lower()
  print()

print(f'Voce escolheu {arma}.')
print()

# Atribui os devidos valores à cada arma
if arma == 'espada':
  weapon(10, 25, 95, 115, arma)

if arma == 'machado':
  weapon(15, 30, 95, 110, arma)

if arma == 'adaga':
  weapon(5, 25, 95, 120, arma)

if arma == 'arco':
  weapon(25, 30, 95, 105, arma)

if arma == 'sabre magico':
  weapon(5, 10, 100, 100, arma)

# Define algumas estatísticas iniciais do personagem
ouro = 0
vida = 100

avancar()

roll()

if roll_result <= 5:
  monster_encounter('Mula sem cabeça', 30, 5, 20)
  
elif roll_result > 5:
  gold_gain(ouro, 50)