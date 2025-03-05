## Tic-Tac-Toe Game using Python & Tkinter
This is a simple, graphical version of the classic Tic-Tac-Toe game built with Python and the Tkinter library. 
It allows two players (Player 'X' and Player 'O') to take turns making moves on a 3x3 grid. 
The game detects the winner and disables the game buttons once the game is over, with an option to reset the game.

# Features
Player 1 vs Player 2 : Two players can play by clicking the buttons on a 3 x 3 grid.

* The game checks for a winner after every move and highlights the winning combination.
* Game Reset: After the game ends, players can reset the game and start a new round.
* Tie : The game detects if it's a tie and notifies the players.

# Requirements
* Python 3.x
* Tkinter (usually bundled with Python)

# How to Run
* Step 1: Install Python (if not already installed)
Ensure that you have Python 3.x installed on your system. You can download and install Python from the official Python website.

* Step 2: Install Tkinter (if not installed)
Tkinter is generally bundled with Python, but if it's not installed, you can install it using the following command:

    For Linux (Debian/Ubuntu):
    sudo apt-get install python3-tk
    
    For macOS:
    brew install python-tk
    
    For Windows, Tkinter is usually included by default with Python installation.

* Step 3: Save the Code
Copy the code into a Python file, for example, tic_tac_toe.py.

* Step 4: Run the Game
Open a terminal or command prompt, navigate to the directory where you saved the file, and run:

* Step 5: Playing the Game
    The game starts with an empty 3x3 grid of buttons.
    Player X starts first, followed by Player O.
    Players alternate clicks on the grid to place their marks ("X" or "O").
    The game will announce the winner or a tie and disable further moves.
  
    You can reset the game using the “Reset” option from the menu.

python tt_toe.py
This will launch a GUI window for the Tic-Tac-Toe game.
