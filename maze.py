import time
import random
from cell import Cell
from graphics import Window, Line, Point

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window | None = None, seed: int | None = None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells: list[list[Cell]] = []
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_end_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j) -> None:
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (j * self._cell_size_y)
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_end_exit(self) -> None:
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _reset_cells_visited(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            self._break_walls_r(next_index[0], next_index[1])
