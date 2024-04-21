from graphics import Line, Point, Window

class Cell:
    def __init__(self, win: Window) -> None:
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        line_color = "grey" if undo else "red"
        start = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        end = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        self._win.draw_line(Line(start, end), line_color)
