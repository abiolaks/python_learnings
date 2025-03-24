class House:
    """_summary_: creating a House object with  for wall area

        Args:
        wall_area (float): wall area of the house
        
    """
    def __init__(self, wall_area):
        self.wall_area = wall_area
        
        
# creatting a paint class
class Paint:
    """_summary_: creating a paint object with buckets needed and color
    
        Args:
        buckets(integer): number of buckets needed to paint the house
        color (string): color of the paint
    """
    
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color