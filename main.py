acceptable_choice = ['X', 'O']

player1name=input("Enter your name ")
player1name=player1name.capitalize()
player2name=input("Enter your name ")
player2name=player2name.capitalize()

player1 = input(player1name +" enter 'X' or 'O': ")
player1 = player1.upper()
player2 = 'O'
while player1 not in acceptable_choice:
    player1 = input("You have to enter 'X' or 'O'. Player 1's turn, enter 'X' or 'O': ")

def p1choice(valtozo1):
    if valtozo1 == 'X':
        valtozo2 = 'O'
    else:
        valtozo2 = 'X'
    return valtozo2

player2=(p1choice(player1))
print(player1name+':'+player1)
print(player2name+':'+player2)


table=[['_','_','_'],['_','_','_'],['_','_','_']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()








def givep1place():
    p1place=int(input(player1name+' enter a number from 1-9 '))
    while p1place <1 or p1place > 9:
        print('Incorrect number, please try again')
        p1place = int(input(player1name + ' enter a number from 1-9 '))
    return p1place

p1place=givep1place()

#table[(player1-1)/3][(player1-1)%3]=player1

match p1place:
    case 1:
      if table[0][0] in acceptable_choice:
          print(player1name+' don\'t cheat')
          p1place=givep1place()
      else:
          table[0][0]=player1
    case 2:
      table[0][1]=player1
    case 3:
      table[0][2]=player1
    case 4:
      table[1][0]=player1
    case 5:
      table[1][1]=player1
    case 6:
      table[1][2]=player1
    case 7:
      table[2][0]=player1
    case 8:
      table[2][1]=player1
    case 9:
      table[2][2]=player1

for row in table:
    for cell in row:
        print(cell, '', end='')
    print()


def givep2place():
    p2place = int(input(player2name + ' enter a number from 1-9 '))
    while p2place < 1 or p2place > 9:
        print('Incorrect number, please try again')
        p2place = int(input(player2name + ' enter a number from 1-9 '))
    return p2place


p2place = givep2place()

# table[(player1-1)/3][(player1-1)%3]=player1

match p2place:
    case 1:
        table[0][0] = player2
    case 2:
        table[0][1] = player2
    case 3:
        table[0][2] = player2
    case 4:
        table[1][0] = player2
    case 5:
        table[1][1] = player2
    case 6:
        table[1][2] = player2
    case 7:
        table[2][0] = player2
    case 8:
        table[2][1] = player2
    case 9:
        table[2][2] = player2

for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

print('Round over')






