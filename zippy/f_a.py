'''
f_a.py
'''

from point import Point
import numpy as np
from utils import sign, f3sqrt

class F_a:

    '''
    The map f_a as defined in the Geodisc algorithm.
    '''

    def __init__(self, a):
        '''
        Constructor.
        Parameters:
        a (complex): the boundary of the shape is from the origin to a
        '''

        self.a = a
        self.b = np.abs(a) / a.real
        self.c = np.abs(a) / a.imag

    def f1(self, p: Point) -> Point:
        '''
        Applies the Mobius map f_1(z) = \frac{z}{1- \frac{z}{b}}
        to the given point.
        Parameters:
        p (Point): point to apply map to
        Returns:
        Point: f_1(p.z)
        '''

        # f_1(b) = \inf
        if p.z == 0:
            return None # FIXME: How do we want to handle this?
        
        # f_1(a) = 0
        elif p.z == self.a:
            return Point(z = complex(0, 0),
                         is_origin = True,
                         name = p.name,
                         branch_sign = 0) # It does not matter what branch_sign is

        # Otherwise, map is applied as usual
        else:
            z = p.z / (1 - p.z / self.b)
            return Point(z = z,
                         is_origin = False,
                         name = p.name,
                         branch_sign = sign(z))

    def f2(self, p: Point) -> Point:
        '''
        Applies the map f_2(z) = z^2 + c^2 to the given point.
        Parameters:
        p (Point): point to apply map to
        Returns:
        Point: f_2(p.z)
        '''
        z = p.z ** 2 + self.c ** 2

        # Update the flag if the point lands at the origin
        is_origin = (z == complex(0, 0))

        return Point(z = z,
                     is_origin = is_origin,
                     name = p.name,
                     branch_sign = p.branch_sign)

    def f3(self, p: Point) -> List[Point]:
        '''
        Applies the map f_3(z) = \sqrt{z} with the branch
        cut along the real axis.
        Parameters:
        p (Point): point to apply map to
        Returns:
        List[Point]: f_3(z), result of map, potentially multivalued
        '''
        pass