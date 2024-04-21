from graphics import Line, Point, Window

class Cell:
    def __init__(self, win: Window | None = None) -> None:
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self._win is None:
            return
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(left_wall, "black" if self.has_left_wall else "white")


        right_wall = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(right_wall, "black" if self.has_right_wall else "white")

        top_wall = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(top_wall, "black" if self.has_top_wall else "white")

        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(bottom_wall, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        line_color = "grey" if undo else "red"
        start = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        end = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        if self._win is not None:
            self._win.draw_line(Line(start, end), line_color)
