from numpy import array, empty, float32, extract


class Point:

    def __init__(self):
        self.curve_points = None
        self.selected_index = None

        self.x = self.y = 0
        self.start_x = self.end_y = 50
        self.end_x = self.start_y = 560

        self.start_point = (self.start_x, self.start_y)
        self.end_point = (self.end_x, self.end_y)

        self.points = [self.start_point, self.start_point, (150, 200), (250, 100), self.end_point, self.end_point]

        self.lim = {
            'x': 8,
            'y': 63,
            'dist_remove': 6
        }

    # tk.Canvas
    def create_oval(*args, **kwargs):
        pass

    # def distance_axis(self, i, index_axis, event_var):
    #     return abs(self.points[i][index_axis] - event_var)

    @staticmethod
    def distance_one(*args, **kwargs):
        pass
        return 0

    def distance(*args, **kwargs):
        pass
        return 0

    # adding rules
    def allow_add_point(self, event):
        x, y = event.x, event.y

        # rule 1: event.y limit grid
        if y > self.start_y or y < self.end_y:
            return 0

        # rule 2: event.x > points[1].x; event.x < point[-2].x
        if x < self.points[1][0] or x > self.points[-2][0]:
            return 0

        # rule 3: |event.x - exist_point.x| >= 8
        size_p = len(self.points)
        distances_x = empty(shape=(size_p,), dtype=float32)

        for i in range(size_p):
            distances_x[i] = abs(self.points[i][0] - x)

            if distances_x[i] < self.lim['x']:
                return 0

        # rule 4: |event.y - curve_coords.y where event.x == curve_coords.x| < 64

        np_curve_points = array(self.curve_points)
        range_event = np_curve_points[np_curve_points[:, 0].astype(int) == x]
        near_point = max(range_event, key=lambda c: c[1])

        if abs(y - near_point[1]) > self.lim['y']:
            return 0

        return 1

    def draw_point(self, x, y):
        return self.create_oval(x-3, y-3, x+3, y+3, fill="#aaaaaa", outline="black", tags="point")

    def add_point(self):
        self.points.append((self.x, self.y))
        self.points = sorted(self.points, key=lambda c: c[0])

    def limited_point(self, formula):
        self.x = formula
        self.points[self.selected_index] = (formula, self.y)

    def choose_point(self, event):
        # choose the nearest point
        index = min(range(len(self.points)), key=lambda i: self.distance(i, event.x, event.y, self.points))
        self.selected_index = min(max(1, index), len(self.points) - 2)
        return self.points[self.selected_index]

    def remove_point(self):
        # remove a point from the list
        self.points = [point for index, point in enumerate(self.points) if index != self.selected_index]

    def allow_influence_point(self, event):
        # define index & point
        point = self.choose_point(event)

        # rule 1: side points -> const
        if self.selected_index in (1, len(self.points) - 2):
            return 0

        # rule 2: distance_remove < 7 => between point & "coords click"
        distance = self.distance_one(*point, event.x, event.y)

        if distance > self.lim['dist_remove']:
            return 0

        return 1

