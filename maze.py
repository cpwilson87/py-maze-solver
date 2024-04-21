import time
from cell import Cell
from graphics import Window, Line, Point

class Maze:
    def __init__(self, x1: int, y1: int, num_cols: int, num_rows: int, cell_size_x: int, cell_size_y: int, win: Window) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells: list[list[Cell]] = []
        self._win = win
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j) -> None:
        x1 = self._x1 + (i * self._cell_size_x)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (j * self._cell_size_y)
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(0.05)
