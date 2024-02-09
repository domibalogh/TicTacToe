acceptable_choice = ['X', 'O']
numbers= ['1','2','3','4','5','6','7','8','9']

player1name=input("Enter your name ")
player1name=player1name.capitalize()
player2name=input("Enter your name ")
player2name=player2name.capitalize()



player1 = input(player1name +" enter 'X' or 'O': ")
player1 = player1.upper()
player2 = 'O'
while player1 not in acceptable_choice:
    player1 = input("You have to enter 'X' or 'O'. Player 1's turn, enter 'X' or 'O': ")
    player1 = player1.upper()

def p1choice(valtozo1):
    if valtozo1 == 'X':
        valtozo2 = 'O'
    else:
        valtozo2 = 'X'
    return valtozo2

def givep1place():
    p1place=(input(player1name+' enter a number from 1-9 '))
    while p1place not in numbers:
        print("belepett")
        p1place = (input(player1name + ' enter a number from 1-9 '))
    p1place=int(p1place)
    return p1place

def givep2place():
    p2place = (input(player2name + ' enter a number from 1-9 '))
    while p2place not in numbers:
        p2place = (input(player2name + ' enter a number from 1-9 '))
    p2place = int(p2place)
    return p2place

player2=(p1choice(player1))
print(player1name+':'+player1)
print(player2name+':'+player2)


table=[['_','_','_'],['_','_','_'],['_','_','_']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()








finalwinner=''
listx=['X']
listo=['O']
list=['X', 'O']
gamewon=False
response2=True
accresponse=['Yes', 'No']

while response2==True:
    def winner():
        if (table[0][0]==table[0][1]==table[0][2] in listo or
          table[1][0]==table[1][1]==table[1][2]in listo or
          table[2][0]==table[2][1]==table[2][2]in listo or
          table[0][0]==table[1][1]==table[2][2]in listo or
          table[2][0] == table[1][1] == table[0][2]in listo or
          table[0][0] == table[1][0] == table[2][0]in listo or
          table[0][1] == table[1][1] == table[2][1]in listo or
          table[0][2] == table[1][2] == table[2][2]in listo or
          table[0][0] == table[0][1] == table[0][2] in listx or
          table[1][0] == table[1][1] == table[1][2] in listx or
          table[2][0] == table[2][1] == table[2][2] in listx or
          table[0][0] == table[1][1] == table[2][2] in listx or
          table[2][0] == table[1][1] == table[0][2] in listx or
          table[0][0] == table[1][0] == table[2][0] in listx or
          table[0][1] == table[1][1] == table[2][1] in listx or
          table[0][2] == table[1][2] == table[2][2] in listx):
            return True
        else:
            return False




    def check_elements(table):
        return all(cell != '_' for row in table for cell in row)






    while gamewon==False:



        p1place=givep1place()

        #table[(player1-1)/3][(player1-1)%3]=player1
        match p1place:
            case 1:

                while table[0][0] in acceptable_choice and p1place == 1:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 2:

                while table[0][1] in acceptable_choice and p1place == 2:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 3:

                while table[0][2] in acceptable_choice and p1place == 3:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 4:

                while table[1][0] in acceptable_choice and p1place == 4:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 5:

                while table[1][1] in acceptable_choice and p1place == 5:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 6:

                while table[1][2] in acceptable_choice and p1place == 6:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 7:

                while table[2][0] in acceptable_choice and p1place == 7:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 8:

                while table[2][1] in acceptable_choice and p1place == 8:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()
            case 9:
                while table[2][2] in acceptable_choice and p1place == 9:
                    print(player1name + ' do not cheat')
                    p1place = givep1place()



        match p1place:
            case 1:
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

        gamewon = winner()
        if gamewon == True:
            finalwinner=player1name
            print(finalwinner + ' is the winner')
            break

        if check_elements(table):
            print("Nobody wins")
            break

        p2place = givep2place()

        # table[(player1-1)/3][(player1-1)%3]=player1

        match p2place:
            case 1:

                while table[0][0] in acceptable_choice and p2place == 1:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 2:

                while table[0][1] in acceptable_choice and p2place == 2:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 3:

                while table[0][2] in acceptable_choice and p2place == 3:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 4:

                while table[1][0] in acceptable_choice and p2place == 4:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 5:

                while table[1][1] in acceptable_choice and p2place == 5:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 6:

                while table[1][2] in acceptable_choice and p2place == 6:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 7:

                while table[2][0] in acceptable_choice and p2place == 7:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 8:

                while table[2][1] in acceptable_choice and p2place == 8:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()
            case 9:
                while table[2][2] in acceptable_choice and p2place == 9:
                    print(player2name + ' do not cheat')
                    p2place = givep2place()




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

        gamewon=winner()

        if gamewon == True:
            finalwinner = player2name
            print(finalwinner + ' is the winner')
            break


        if check_elements(table):
            print("Nobody wins")
            break



    response=input('Do you want to play again?')
    response=response.capitalize()


    while response not in accresponse:


        response = input('Do you want to play again?')
        response = response.capitalize()



    if response=='Yes':
        gamewon=False
        table = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        response2=True
    else:
        response2=False









