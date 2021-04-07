from math import sqrt

import cv2
import numpy as np

class Polygon:
    def __init__(self, contour):
        self._contour = contour

    def is_inside(self, point):
        return cv2.pointPolygonTest(self._contour, point, measureDist=False) >= 0

    def area_measurement(self):
        return cv2.contourArea(self._contour)

    def centroid(self):
        contour = np.array(self._contour)
        x_mean = sum(contour[:, 0]) / len(contour)
        y_mean = sum(contour[:, 1]) / len(contour)
        return x_mean, y_mean


class Rectangle(Polygon):
    def __init__(self, contour):
        super().__init__(contour)
        self.upper_right = contour[1]
        self.lower_left = contour[2]

    def is_inside(self, point):
        return self.lower_left[0] <= point[0] <= self.upper_right[0] \
            and self.lower_left[1] <= point[1] <= self.upper_right[1]

    def area_measurement(self):
        return (self.upper_right[0] - self.lower_left[0]) \
               * (self.upper_right[1] - self.lower_left[1])

    def centroid(self):
        return ((self.upper_right[0] + self.lower_left[0]) /2,
                (self.upper_right[1] + self.lower_left[1]) /2)

class Triangle(Polygon):
    def __init__(self, contour):
        super().__init__(contour)

    def area_measurement(self):
        vectors = [(self._contour[i - 1][0] - self._contour[i][0],
                    self._contour[i - 1][1] - self._contour[i][1])
                   for i in range(len(self._contour))]

        a, b, c = map(lambda x: sqrt(x[0]x[0] + x[1]x[1]), vectors)
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))
