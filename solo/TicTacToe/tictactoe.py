# Tic Tac Toe
import random

y_array1 = [" "," "," "]
y_array2 = [" "," "," "]
y_array3 = [" "," "," "]
x_array = [y_array1,y_array2,y_array3]

#[i] = y_array# [j] = in y_array

def disp_board():
    board_hor = "  1   2   3"
    board_ver = ["A","B","C"]
    print board_hor
    for i in range(3):
        print board_ver[i],
        for j in range(3):
            print x_array[i][j],
            if j < 2:
                print "|",
        if i < 2:
            print
            print "  ---------"
        

def get_move_human():
    valid_move = 0;
    ver = ["a","b","c"]
    print
    print "--== Human Move ==--"
    while(valid_move == 0):
        user_hor = raw_input("Column    (1,2,3): ")
        user_ver = raw_input("Row       (A,B,C): ").lower()
        print "Your Choice: " + user_hor + user_ver
        try:
            if(0 <= int(ver.index(user_ver)) <= 2 and 0 <= int(user_hor)-1 <= 2):
                if(x_array[int(ver.index(user_ver))][int(user_hor)-1] == " "):
                    x_array[int(ver.index(user_ver))][int(user_hor)-1] = "X"
                    valid_move = 1;
                else:
                    print "That spot is already taken."
            else:
                print "That is not a valid move."
        except:
            print "Something went wrong, try again."
    

def check_end(player): #player 0=User 1=Computer
    global running
    player_list = ["Human","Computer"]


    #Hor
    for j in range(3):
            if(x_array[j][0] == x_array[j][1] == x_array[j][2] \
               and x_array[j][0] != " "):

                print player_list[player] + " victory at Row ", j+1 , "."
 
                running = 0
    #Ver
    for j in range(3):
            if(x_array[0][j] == x_array[1][j] == x_array[2][j] \
               and x_array[0][j] != " "):
                
                print player_list[player] + " victory at Column ", j+1 , "."
                running = 0

    #diag
    if(x_array[0][0]==x_array[1][1] == x_array[2][2] != " " \
       or x_array[0][2] == x_array[1][1] == x_array [2][0] != " "):

       print player_list[player] + " diagonal victory."
       running = 0
       
                

def get_move_computer():

    print
    print "--== Computer Move ==--"
    
    xo_list = ["O","X"]
    spot_in_row =[" "," "," "]
    
    if(x_array[1][1] == " "):
        #Take center if free
        x_array[1][1] = "O" 
    elif(game_round == 1 and x_array[1][1] == "X"):
        #Human takes center (on first turn)
        x_array[0][0] = "O"
    else:
        for k in range(2):
            print k
                #diagonal based move
            if(x_array[0][0] == x_array[1][1] == xo_list[k] and x_array[2][2] == " "):
                x_array[2][2] = "O"
                break
            elif(x_array[1][1] == x_array[2][2] == xo_list[k] and x_array[0][0] == " "):
                x_array[0][0] = "O"
                break
            elif(x_array[0][2] == x_array[1][1] == xo_list[k] and x_array[2][0] == " "):
                x_array[2][0] = "O"
                break
            elif(x_array[1][1] == x_array[2][0] == xo_list[k] and x_array[0][2] == " "):
                x_array[0][2] = "O"
                break
                
            else:
                for j in range(3):
                    for k in range(2):
                        #hor based move
                        if(x_array[j][0] == x_array[j][1] == xo_list[k] and x_array[j][2] == " "): 
                            x_array[j][2] = "O"
                            break
                        elif(x_array[j][1] == x_array[j][2] == xo_list[k] and x_array[j][0] == " "):
                            x_array[j][0] = "O"
                            break
                        #ver based move
                        elif(x_array[0][j] == x_array[1][j] == xo_list[k] and x_array[2][j] == " "):
                            x_array[2][j] = "O"
                            break
                        elif(x_array[1][j] == x_array[2][j] == xo_list[k] and x_array[0][j] == " "):
                            x_array[0][j] = "O"
                            break
                        #offensive moves
                        elif(x_array[0][1] == " "):
                            x_array[0][1] = "O"
                            break
                        elif(x_array[1][0] == " "):
                            x_array[0][1] == "O"
                            break
                        else:
                            print "rand move"
                            while():
                                num1 = random.randint(0,3)
                                num2 = random.randint(0,3)
                                if(x_array[num1][num2] == " "):
                                    x_array[num1][num2] = "O"
                                    break
                            break
                    break
                                
                
           

       
def game_over():
    print
    print
    print "Game Over"
            
        
    

    


# Main Loop
game_round = 0
player_turn = 0 #0=human, 1= comp
running = 1
while(running == 1):
    #Prints the board
    disp_board()
    
    #Player's take turns
    if(player_turn == 0):
        get_move_human()
    elif(player_turn == 1):
        get_move_computer()

    #Check for winning move
    check_end(player_turn)

    #Change player turn
    if(player_turn == 0):
        player_turn = 1
    elif(player_turn == 1):
        player_turn = 0
    else:
        print "Error: Player turn switch"

    game_round += 1
disp_board()
game_over()



        
    
    

        
