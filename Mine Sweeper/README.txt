MINE SWEEPER 10x10x10
------------------------------------------------------------------------
This file contains the instructions for running the program as well as
the controls and capabilities given to the user.
------------------------------------------------------------------------
STARTUP INSTRUCTIONS
------------------------------------------------------------------------
First time start up is opening the terminal and changing the directory
to the location where file 'start.py' is located. Then running the line
"python3 start.py" will open the window containing the program. You must
have python installed onto your path or else you will recieve an error
and you must install the PyQt5 module as well. You can do so by calling
the command "pip install pyqt5" in Windows Shell or "sudo apt install
pyqt5" for Linux.
------------------------------------------------------------------------
GAMEPLAY INSTRUCTIONS
------------------------------------------------------------------------
To play minesweeper, you will click squares across the grid to reveal
certain values that pertain to that square. If its a number, that is
the number of mines in the grids that are adjacent to it. To win, you
must reveal every square that isn't a mine without clicking on a mine.
If you do, the game will end in a loss. To reset the game, simply click
the Reset Game button. We will keep track of wins, losses, and win loss
ratio, as well as the number of moves made in that game.

Reveal: [LEFT_CLICK]
Flag: [SHIFT] + [LEFT CLICK]

------------------------------------------------------------------------
