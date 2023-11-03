#Simple game of tic tac toe
#Version 1 will have all methods defined in one file
#Is intended to be functional but lots of room for improvement
import os

def main():

    #start of definitions
    game_board = [[],[],[]]
    keep_playing = True
    X_player_turn = True
    valid_move = False
    turn_count = 0

    def setup_board():
        game_board[0] = ["1","2","3"]
        game_board[1] = ["4","5","6"]
        game_board[2] = ["7","8","9"]
        return game_board

    def display_board():
        os.system('cls')
        #print(game_board)
        print(str(game_board[0][0]) + "|" + str(game_board[0][1]) + "|" + str(game_board[0][2]))
        print("-----")
        print(str(game_board[1][0]) + "|" + str(game_board[1][1]) + "|" + str(game_board[1][2]))
        print("-----")
        print(str(game_board[2][0]) + "|" + str(game_board[2][1]) + "|" + str(game_board[2][2]))
    
    def check_input(input):
        if input >= 1 or input <=10:
            return True
        else:
            return False
        
    def valid_place(input):
        if input >= 1 and input <=3 and str(game_board[0][input-1]) != 'O' and str(game_board[0][input-1]) != 'X':
            return True
        elif input >= 4 and input <=6 and str(game_board[1][input-4]) != 'O' and str(game_board[1][input-4]) != 'X':
            return True
        elif input >= 7 and input <=9 and str(game_board[2][input-7]) != 'O' and str(game_board[2][input-7]) != 'X':
            return True
        else:
            return False
        
    def get_row(input):
        if int(input) >= 1 and input <=3:
            return 0
        elif input >= 4 and input <=6:
            return 1
        elif input >= 7 and input <=9:
            return 2

    def get_col(input):
        if input in [1,4,7]:
            return 0
        elif input in [2,5,8]:
            return 1
        elif input in [3,6,9]:
            return 2
        
    def check_victory():
        #check rows
        if game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X':
            return True 
        elif game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X':
            return True
        elif game_board[2][0] == 'X' and game_board[2][1] == 'X' and game_board[2][2] == 'X':
            return True
        #check columns
        elif game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X':
            return True
        elif game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X':
            return True
        elif game_board[0][2] == 'X' and game_board[1][2] == 'X' and game_board[2][2] == 'X':
            return True
        #check cross
        elif game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X':
            return True
        elif game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X':
            return True
        #check for O victory
        #check rows
        elif game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O':
            return True 
        elif game_board[1][0] == 'O' and game_board[1][1] == 'O' and game_board[1][2] == 'O':
            return True
        elif game_board[2][0] == 'O' and game_board[2][1] == 'O' and game_board[2][2] == 'O':
            return True
        #check columns
        elif game_board[0][0] == 'O' and game_board[1][0] == 'O' and game_board[2][0] == 'O':
            return True
        elif game_board[0][1] == 'O' and game_board[1][1] == 'O' and game_board[2][1] == 'O':
            return True
        elif game_board[0][2] == 'O' and game_board[1][2] == 'O' and game_board[2][2] == 'O':
            return True
        #check cross
        elif game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O':
            return True
        elif game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O':
            return True
        #no hits return false
        else:
            return False
    
    def another_game():
        ag = ""
        while ag != "yes" and ag != "no":
            ag = input("Play again (yes/no): ")
        
        if ag == "yes":
            return True
        elif ag == "no":
            return False
        else:
            print("how?")
            return False

        
    #end of definitions
    #start of application code


    game_board = setup_board()
    while keep_playing:
        while not valid_move:
            display_board()
            turn_count += 1
            if turn_count == 10:
                display_board()
                print("The game was a draw!")
                keep_playing = another_game()
                break
            elif X_player_turn:
                move = input("X Enter a number 1 - 9 (10 to quit): ")
                valid_move = valid_place(int(move))
                if check_input(int(move)) and int(move) != 10 and valid_move:
                    game_board[get_row(int(move))][get_col(int(move))] = 'X'
                    if check_victory():
                        display_board()
                        print("X player wins!")
                        keep_playing = another_game()
                        break
                    X_player_turn = False
                elif move == "10":
                    keep_playing = False
                    break
                        
            else:
                move = input("O Enter a number 1 - 9 (10 to quit): ")
                valid_move = valid_place(int(move))
                if check_input(int(move)) and int(move) != 10 and valid_move:
                    game_board[get_row(int(move))][get_col(int(move))] = 'O'
                    if check_victory():
                        display_board()
                        print("O player wins!")
                        keep_playing = another_game()
                        break
                    X_player_turn = True
                elif move == "10":
                    keep_playing = False
                    break

            valid_move = False         

        if keep_playing == False:
            os.system('cls')
            print("thanks for playing, exiting.")
            break
        elif keep_playing == True:
            game_board = setup_board()
            valid_move = False
            turn_count = 0
        
if __name__ == "__main__":
    main()