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

    def __init__(self, a: complex):
        '''
        Constructor.
        Parameters:
        a (complex): the base point of the map
        '''

        self.a = a.z
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
        
        
        # FIXME: is it possible that a point very close to the actual base point a
        # could be interpreted as that a that defines this particular map?
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

        # Note that we do not update the is_origin flag, as
        # it is possible for a different point to land at the origin,
        # but this flag is only used for internal detection of the base point a

        return Point(z = z,
                     is_origin = p.is_origin,
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
        Raises:
        ValueError if the origin is encountered without is_origin flag
        '''

        if p.z == 0 and not p.is_origin:
            raise ValueError("Unexpected: zero encountered in f3 from non-origin point.")

        if p.is_origin:
            sqrt_val = f3sqrt(p.z)
            return [
                Point(z = sqrt_val, is_origin = False, name = p.name, branch_sign = 1),
                Point(z = sqrt_val, is_origin = False, name = p.name, branch_sign = -1)
            ]
        else:
            sign = p.branch_sign if p.branch_sigh != 0 else 1
            sqrt_val = sign * f3sqrt(pt.z)
            return [
                Point(z = sqrt_val, is_origin = False, branch_sign = sign, name = p.name)
            ]