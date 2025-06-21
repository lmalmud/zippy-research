'''
point.py
'''

import warnings

class Point:
    '''
    Defines a point that represents one of the points
    along the boundary of the shape.
    '''

    def __init__(self,
                 z: complex,
                 *,
                 name: str = None,
                 is_origin: bool = None,
                 on_axis: bool = None,
                 on_arc: bool = False,
                 branch_sign: int = 0):
        '''
        Constructor.
        Parameters
        z (complex): location of the point
        name (str): the name of the point, otherwise initialized to the current point
        is_origin (bool): whether the original point was the origin
        on_axis (bool): whether the original point was on the real axis
        on_arc (bool): whether the original point was on the arc \gamma from 0 to a
        branch_sign (int): the multiplier that will be applied at the square root
        Raise
        '''

        # FIXME: I think that is_origin may be redundant if we have on_axis

        self.z = z
        self.is_origin = is_origin

        # Ensure that a point is assigned is_origin = True if it the origin and no parameter was given
        if is_origin == None and z == complex(0, 0):
            warnings.warn('An origin point was created without indication is_origin = True')
            self.is_origin = True
        elif is_origin == None:
            self.is_origin = False

        # Ensure that a point is assigned on_axis = True if it is on the real axis and no parameter was given
        self.on_axis = on_axis
        if on_axis == None and z.imag == 0:
            warnings.warn('A point on the real axis was created wihtout indication that on_axis = True')
            self.on_axis = True
        elif on_axis == None:
            self.on_axis = False

        # These parameters will default to non-multivalued behavior
        self.on_arc = on_arc
        self.branch_sign = branch_sign

        # If no name is provided, the name of the point will be the location given
        if name == None:
            self.name = str(z)
        else:
            self.name = name