from graphics import Point, Window, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(1, 1, 4, 3, 100, 100, win)

    win.wait_for_close()

main()
