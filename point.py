# Creating a  point class
class Point:
    def __init__(self, x, y):
        """Summary: Minimum requirement needed create to create a point object
        

        Args:
            x (integer): x-coordinate
            y (integer): y-coordinate
        """
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
        
    def distance_from_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5
    
    # more succint way of getting the distance between two points passing point objects
    def distance_from_points(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        