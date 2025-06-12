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
                 is_origin: bool = None,
                 branch_sign: int = 0):
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

        # Ensure that a point is assigned to be the origin if it is and no parameter
        # was given
        if is_origin == None and z == complex(0, 0):
            self.is_origin = True
        elif is_origin == None:
            self.is_origin = False
            
        self.branch_sign = branch_sign

        # If no name is provided, the name of the point will be the location given
        if name == None:
            self.name = str(z)
        else:
            self.name = name