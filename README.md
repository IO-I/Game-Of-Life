# Game of Life
This repository contains a simple implementation of Conway's Game of Life using Python and Pygame.

## Rules of the Game
The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is played on a two-dimensional grid of cells, each of which can be in one of two states: alive or dead. The grid evolves over time, with the state of each cell at time t+1 depending on the state of its eight neighbors at time t, according to the following rules:

Any live cell with fewer than two live neighbors dies, as if by underpopulation.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Requirements
Python 3.x

Pygame

## How to Run
Clone the repository to your local machine.
Install Pygame by running pip install pygame in your terminal.
Run the code using python game_of_life.py in your terminal.

## Usage
Once you run the code, a Pygame window will open displaying the game board. The board is initialized with random live and dead cells.

You can change the size of the board by changing the values of GRID_WIDTH and GRID_HEIGHT variables. The CELL_SIZE variable determines the size of each cell in pixels.

You can also adjust the speed of the game by changing the value of clock.tick(20) line. The current value is set to 20 FPS.

## Acknowledgments
This implementation is inspired by Daniel Shiffman's Coding Challenge on YouTube.
