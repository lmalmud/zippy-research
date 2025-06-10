'''
point.py
'''

class Point:
    '''
    Defines a point that represents one of the points
    along the boundary of the shape.
    '''

    def __init__(self,
                 z: complex,
                 name: str = None,
                 is_origin: bool = False,
                 branch_sign: int = 1):
        '''
        Constructor.
        Parameters
        z (complex): location of the point
        name (str): the name of the point, otherwise initialized to the current point
        is_origin (bool): whether the current point is the origi
        branch_sign (int): the multiplier that will be applied at the square root
        '''

        self.z = z
        self.is_origin = is_origin
        self.branch_sign = branch_sign

        # If no name is provided, the name of the point will be the location given
        if name == None:
            self.name = str(p)
        else:
            self.name = name