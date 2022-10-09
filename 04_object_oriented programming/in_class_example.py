class Marker:

    def __init__(self, color, point, l, d):  # define the function / constructor
        # constructor are the values to c
        self.color = color
        self.point = point
        self.l = l
        self.d = d
        self.ink = 1

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_point(self):
        return self.point

    def set_point(self, point):
        self.point = point

    def dimensions(self):
        return self.l, self.d


# print('_'*30, 'RED MARKER', '_'*30)
red_marker = Marker('Red', 'Fine', 4, .2)  # applies attributes
print(red_marker.get_color(), red_marker.get_point())  # returns the color of red marker and the point
l, d = red_marker.dimensions()  # unpacks red
print(l, d)
