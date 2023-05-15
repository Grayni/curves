from numpy import empty, float32


class Point:
    def __init__(self):
        self.points = None
        self.x = None
        self.y = None
        self.selected_index = None
        self.curve_points = None
        self.x_lim = None
        self.y_lim = None

    # tk.Canvas
    def create_oval(*args, **kwargs):
        pass

    def distance_axis(self, i, index_axis, event_var):
        return abs(self.points[i][index_axis] - event_var)

    # adding rules
    def allow_add_point(self, event):

        # rule 1: |event.x - exist_point.x| >= 8
        size_p = len(self.points)
        distances_x = empty(shape=(size_p,), dtype="float32")

        for i in range(size_p):
            distances_x[i] = abs(self.points[i][0] - event.x)

            if distances_x[i] < self.x_lim:
                return 0

        # rule 2: |event.y - curve_coords.y where event.x == curve_coords.x| < 64
        size_c = len(self.curve_points)
        distances_y = empty(shape=(size_c,), dtype="float32")

        print(type(self.curve_points))

        for i in range(size_c):
            distances_y[i] = abs(self.curve_points[i][1] - event.y)

            if distances_y[i] < self.y_lim:
                self.add_point(event.x, event.y)
                return 0



        self.add_point(event.x, event.y)

    def draw_point(self, x, y):
        return self.create_oval(x-3, y-3, x+3, y+3, fill="#aaaaaa", outline="black", tags="point")

    def add_point(self, x, y):

        self.points.append((x, y))
        self.points = sorted(self.points, key=lambda c: c[0])
        #self.draw_point(x1, y1)

    def limited_point(self, formula):
        self.x = formula
        self.points[self.selected_index] = (formula, self.y)

