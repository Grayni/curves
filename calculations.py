from numpy import zeros, linspace


class Calculations:

    @staticmethod
    def second_derivative(points):
        n = len(points)

        # build the ternary system
        # (assume 0 boundary conditions: y2[0]=y2[-1]=0)
        matrix = zeros((n, 3))
        result = zeros(n)
        matrix[0, 1] = 1
        for i in range(1, n - 1):
            matrix[i, 0] = (points[i][0] - points[i - 1][0]) / 6
            matrix[i, 1] = (points[i + 1][0] - points[i - 1][0]) / 3
            matrix[i, 2] = (points[i + 1][0] - points[i][0]) / 6
            result[i] = (points[i + 1][1] - points[i][1]) / (points[i + 1][0] - points[i][0]) - \
                        (points[i][1] - points[i - 1][1]) / (points[i][0] - points[i - 1][0])
        matrix[n - 1, 1] = 1

        # solving pass1 (up->down)
        for i in range(1, n):
            k = matrix[i, 0] / matrix[i - 1, 1]
            matrix[i, 1] -= k * matrix[i - 1, 2]
            matrix[i, 0] = 0
            result[i] -= k * result[i - 1]

        # solving pass2 (down->up)
        for i in range(n - 2, -1, -1):
            k = matrix[i, 2] / matrix[i + 1, 1]
            matrix[i, 1] -= k * matrix[i + 1, 0]
            matrix[i, 2] = 0
            result[i] -= k * result[i + 1]

        # return second derivative value for each point P
        y2 = result / matrix[:, 1]
        return y2

    def curve_coords(self, points):
        # Spline Curve Interpolation
        sd = self.second_derivative(points)

        # Creating an array of new points
        x_vals = [p[0] for p in points]
        x_curve = linspace(x_vals[0], x_vals[-1], num=1000, endpoint=True)

        # values y for curve
        y_curve = []
        for x in x_curve:
            for i in range(len(points) - 1):
                current = points[i]
                after_cur = points[i + 1]

                if current[0] <= x <= after_cur[0]:
                    t = (x - current[0]) / (after_cur[0] - current[0])
                    a = 1 - t
                    b = t
                    h = after_cur[0] - current[0]
                    y = a * current[1] + b * after_cur[1] + (h**2 / 6) * ((a**3 - a) * sd[i] + (b**3 - b) * sd[i + 1])
                    y_curve.append(y)

        # list curve points
        return list(zip(x_curve, y_curve))

