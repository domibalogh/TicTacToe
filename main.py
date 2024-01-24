


acceptable_choice = ['X', 'O']

player1 = input("Player 1's turn, enter 'X' or 'O': ")
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
print('Player 1 : ',player1)
print('Player 2 : ',player2)


table=[['_','_','_'],['_','_','_'],['_','_','_']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
print("szia")





print('Round over')






