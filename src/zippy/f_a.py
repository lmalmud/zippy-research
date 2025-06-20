'''
f_a.py
'''

from zippy.point import Point
import numpy as np
from typing import List
from zippy.utils import sign, f3sqrt

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
        self.b = (np.abs(self.a) ** 2) / self.a.real
        self.c = (np.abs(self.a) ** 2) / self.a.imag

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
        if p.z == self.b:
            return Point(z=complex(np.inf, 0)) # FIXME: How do we want to handle this?
        
        # Otherwise, map is applied as usual
        else:
            z = p.z / (1 - p.z / self.b)
            return Point(z = z,
                         is_origin = p.is_origin,
                         on_axis = p.on_axis,
                         on_arc = p.on_arc,
                         name = p.name,
                         branch_sign = sign(z))
        
        # FIXME: is it possible that a point very close to the actual base point a
        # could be interpreted as that a that defines this particular map?
        # f_1(a) = 0
        '''
        elif p.z == self.a:
            return Point(z = complex(0, 0),
                         is_origin = True,
                         name = p.name,
                         branch_sign = 0) # It does not matter what branch_sign is
        '''

        

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
                     on_axis = p.on_axis,
                     on_arc = p.on_arc,
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

        '''
        In traditional complex analysis, the output is undefined along the branch cut.
        For this implementation, we allow *both* values along this branch.
        Note that all points that are on the real axis are points that were *originally* on the arc
        '''
        if p.is_origin or p.on_arc:

            # Note that here we are using the standard square root function.
            # When we do not use the standard one, the wrong branch is assigned.
            # The square root function with the branch cut along (0, \infty) is f3sqrt
            sqrt_val = np.sqrt(p.z)
            print(f'the square root value is: {sqrt_val} when the input is {p.z}')
            return [
                Point(z = sqrt_val, is_origin = False, name = p.name, branch_sign = 1),
                Point(z = -sqrt_val, is_origin = False, name = p.name, branch_sign = -1)
            ]
        
        elif p.on_axis:
            
            sqrt_val = p.branch_sign * f3sqrt(p.z)
            return [
                Point(z = sqrt_val, is_origin = False, on_axis = True, branch_sign = p.branch_sign, name = p.name)
            ]
        
        else:
            # Defaults to the principal branch for all non-axis values
            sqrt_val = f3sqrt(p.z)
            return [
                Point(z = sqrt_val, is_origin = False, on_axis = False, branch_sign = sign, name = p.name)
            ]