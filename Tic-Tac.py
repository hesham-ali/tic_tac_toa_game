
import random

"""
Author: Hesham Ali
Client: Electro-PI as a task for python programming master Course
project: involves building a Tic Tac Toe game using Python without a graphical user interface (GUI).


The game will be played on the command line, where the user will enter their moves as text inputs. 
The project will focus on implementing the game logic using Python's built-in data structures and control flow statements. 
The project will include designing the game board as a list of lists, implementing the game logic using if statements and loops,
and creating a simple command-line interface using Python's input() function.
The project will also involve testing and debugging the game to ensure that it functions correctly. 
The game of Tic Tac Toe is played on a 3x3 grid. The players take turns placing their symbol (either X or O) on the grid, 
with the goal of getting three in a row. The game ends when either one player gets three in a row, 
or the grid is full without any player getting three in a row, resulting in a tie. 

Here's a step-by-step decomposition of the game logic: Design the game board as a 3x3 list of lists. 
Each element in the list represents a square on the board and is initially set to an empty string. 
Create a function to print the game board to the console. 
This function should take the game board as a parameter and use loops to iterate through the rows and columns of the board, 
printing each square in the appropriate location. Create a function to handle player moves. 
This function should take the game board and the current player's symbol as parameters, 
prompt the player for their move (using input()), and update the game board with the player's symbol in the appropriate location. 
Create a function to check for a win. 
This function should take the game board and the current player's symbol as parameters and check if any of the rows, 
columns, or diagonals of the board contain three of the player's symbols in a row. 
Create a function to check for a tie. 
This function should take the game board as a parameter and check if every square on the board has been filled. 
Create a main game loop that alternates between the two players. 
In each iteration of the loop, print the current state of the game board, prompt the current player for their move, 
update the game board with the player's symbol, and check if the game has been won or tied. If the game has been won or tied, 
end the loop and print the appropriate message. Test the game by playing it and checking that it correctly handles player moves, 
checks for wins and ties, and prints the appropriate messages. Debug any issues that arise.
"""

game_board = [[" "," "," "],
              [" "," "," "],
              [" "," "," "]]

symbol_lst = ["x","o"]
player = {}
last_symbol = ""
next_symbol =""


def start_game(last_symbol, next_symbol):
    """
        this function for taking players name and his symbol (x,o)
    """
    print("Welcome to tic tac toe game: ")
   
    player1 = input("give me the first player name: ")

    while next_symbol not in symbol_lst:
        next_symbol = input("choose your symbol, it must be (x or o): ").lower()
    
    player[player1]  = next_symbol
       
    player2 = input("give me the second player name: ")
    last_symbol = symbol_lst[symbol_lst.index(next_symbol) -1]
    player [player2] = last_symbol
    return last_symbol, next_symbol
    


def draw_board ():
    for row in range(3):
        print("|",end="")
        for column in range(3):
            print("{}|".format(game_board[row][column]),end="")
        print()    




def check_symbol (last_symbol, next_symbol):
    """
    this function change the next_symbol[0] for the next turn and 
    return the symbol after check if it's right symbol for the player's turn and that it must be (x or o)
    """
    while True:
        symbol = input("Enter your Symbol: ")
        if symbol != next_symbol:
            print("wrong input...!!, your symbol is: ", next_symbol)
        else:
            last_symbol = next_symbol
            next_symbol = symbol_lst[symbol_lst.index(symbol) -1]
            return symbol, last_symbol, next_symbol



def fill_cell (last_symbol, next_symbol):
    """
    this function to fill the cell in the game board after check that chosen cell is empty
    """ 
    while True:
        while True:
            try:
                print("Enter your row And column Number separated by space")
                row, column = [int(x) for x in (input("the row and the column must be <= 3 and > 0: ").split())]
                if row <= 3 and row > 0 and column <= 3 and row > 0:
                    break
            except ValueError:
                print("you must enter two value separated by space")

        if  game_board[row - 1][column - 1] == " " :
            game_board[row - 1][column - 1], last_symbol, next_symbol = check_symbol(last_symbol, next_symbol)
            break
        else:
            print("this cell is been taken, choose another one")

    return row, column, last_symbol, next_symbol


def is_win(row, column):
    
    if any([win_row(row), win_col(column), win_right_diagonal(), win_left_diagonal()]):
        winner = list(filter (lambda x: player[x] == last_symbol, player))[0]
        print(winner," is the winner")
        return True 
        

    

   
        
def win_row (row):
    """
    this function to check if the last turn is the win turn by the row
    and it's only check the row how fill with the last input
    """
    return all([i == last_symbol for i in game_board [row -1]])




def win_col(col):
    """
    this function to check if the last turn is the win turn by the column
    and it's only check the column how fill with the last input
    """
    return all ([row[col -1] == last_symbol for row in game_board])


def win_left_diagonal():
    """
    this function to check if the last turn is the win turn by the right diagonal
    |x| | |
    | |x| |
    | | |x|
    """
    return all(game_board[i][i] == last_symbol for i in range(3))


def win_right_diagonal():
    """
    this function to check if the last turn is the win turn by the left diagonal
    | | |o|
    | |o| |
    |o| | |
    """
    return all(game_board[i][abs(i - 2)] == last_symbol for i in range(3))



last_symbol, next_symbol = start_game(last_symbol, next_symbol)         

for i in range(9): 
    row, column, last_symbol, next_symbol = fill_cell(last_symbol, next_symbol)
    print()
    draw_board()
    print()
    if is_win(row, column):
        break
    elif i == 8:
        print("draw game")
