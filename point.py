from numpy import array, empty, float32, extract


class Point:
    def __init__(self):
        self.points = None
        self.x = None
        self.y = None
        self.selected_index = None
        self.curve_points = None
        self.x_lim = None
        self.y_lim = None
        self.start_y = None
        self.end_y = None

    # tk.Canvas
    def create_oval(*args, **kwargs):
        pass

    def distance_axis(self, i, index_axis, event_var):
        return abs(self.points[i][index_axis] - event_var)

    # adding rules
    def allow_add_point(self, event):

        # rule 1: event.y limit grid
        if self.start_y < event.y or event.y < self.end_y:
            return 0

        # rule 2: event.x > points[1].x; event.x < point[-2].x
        if event.x < self.points[1][0] or event.x > self.points[-2][0]:
            return 0

        # rule 3: |event.x - exist_point.x| >= 8
        size_p = len(self.points)
        distances_x = empty(shape=(size_p,), dtype=float32)

        for i in range(size_p):
            distances_x[i] = abs(self.points[i][0] - event.x)

            if distances_x[i] < self.x_lim:
                return 0

        # rule 4: |event.y - curve_coords.y where event.x == curve_coords.x| < 64

        np_curve_points = array(self.curve_points)
        range_event = np_curve_points[np_curve_points[:, 0].astype(int) == event.x]
        near_point = max(range_event, key=lambda c: c[1])

        if abs(event.y - near_point[1]) > self.y_lim:
            return 0

        self.add_point(event.x, event.y)

    def draw_point(self, x, y):
        return self.create_oval(x-3, y-3, x+3, y+3, fill="#aaaaaa", outline="black", tags="point")

    def add_point(self, x, y):
        self.points.append((x, y))
        self.points = sorted(self.points, key=lambda c: c[0])

    def limited_point(self, formula):
        self.x = formula
        self.points[self.selected_index] = (formula, self.y)

