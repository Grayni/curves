import numpy as np
from math import sqrt


class Calculations:

    # Points distance
    @staticmethod
    def distance_one(x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance(self, i, x, y, points):
        # sqrt((x-points[i][0])**2 + (y-points[i][1])**2)
        return self.distance_one(x, y, *points[i])

    @staticmethod
    def tridiagonal_matrix_algorithm(A, d):
        """
        Solves the linear system of equations Ax = d,
        where A is a tridiagonal matrix of the form:
        [[b1, c1,  0,  0,  0, ... , 0 ],
         [a2, b2, c2,  0,  0, ... , 0 ],
         [ 0, a3, b3, c3, 0, ... , 0 ],
         ...,
         [ 0, ..., 0, a_n-1, b_n-1, c_n-1],
         [ 0, ..., 0,  0,  a_n,  b_n ]]
        and d is the right-hand side vector.
        Uses the Thomas algorithm (also known as the tridiagonal matrix algorithm)
        that solves the system in O(n) time.

        Args:
        A: numpy array of shape (n, 3)
        d: numpy array of shape (n,)

        Returns:
        x: numpy array of shape (n,)
        """
        n = A.shape[0]

        # forward elimination
        for i in range(1, n):
            m = A[i, 0] / A[i - 1, 1]
            A[i, 1] -= m * A[i - 1, 2]
            d[i] -= m * d[i - 1]

        # backward substitution
        x = np.zeros(n)
        x[-1] = d[-1] / A[-1, 1]

        for i in range(n - 2, -1, -1):
            x[i] = (d[i] - A[i, 2] * x[i + 1]) / A[i, 1]

        return x

    def second_derivative(self, points):
        # Get the number of points
        n = len(points)

        # Convert input points to a numpy array
        points = np.array(points)

        # Initialize coefficient matrix and result vector
        matrix = np.zeros((n, 3))
        result = np.zeros(n)

        # Set boundary conditions for second derivative (y2[0] = y2[-1] = 0)
        matrix[0, 1] = 1
        matrix[n - 1, 1] = 1

        # Fill in coefficient matrix
        matrix[1:-1, 0] = (points[1:-1, 0] - points[:-2, 0]) / 6
        matrix[1:-1, 1] = (points[2:, 0] - points[:-2, 0]) / 3
        matrix[1:-1, 2] = (points[2:, 0] - points[1:-1, 0]) / 6

        # Fill in result vector
        result[1:-1] = (points[2:, 1] - points[1:-1, 1]) / (points[2:, 0] - points[1:-1, 0]) - \
                       (points[1:-1, 1] - points[:-2, 1]) / (points[1:-1, 0] - points[:-2, 0])

        # Solve the tridiagonal system of equations using the Thomas algorithm
        y2 = self.tridiagonal_matrix_algorithm(matrix, result)

        # Return array of second derivative values
        return y2

    def curve_coords(self, points):
        # Spline Curve Interpolation
        sd = self.second_derivative(points)

        # Creating an array of new points
        x_vals = np.array([p[0] for p in points], dtype=np.float32)
        x_curve = np.linspace(x_vals[0], x_vals[-1], num=4081, endpoint=True)

        # values y for curve
        y_curve = np.empty_like(x_curve, dtype=np.float32)

        for i in range(len(points) - 1):
            mask = (x_vals[i] <= x_curve) & (x_curve <= x_vals[i + 1])
            x_in_range = x_curve[mask]
            t = (x_in_range - x_vals[i]) / (x_vals[i + 1] - x_vals[i])
            a = 1 - t
            b = t
            h = x_vals[i + 1] - x_vals[i]
            y_in_range = (a * points[i][1] + b * points[i + 1][1] +
                          (h**2 / 6) * ((a**3 - a) * sd[i] + (b**3 - b) * sd[i + 1]))
            # y [50 : 560]
            np.clip(y_in_range, 50, 560, out=y_in_range)
            y_curve[mask] = y_in_range

        return list(zip(x_curve, y_curve))

