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
