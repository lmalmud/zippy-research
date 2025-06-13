'''
test_component_maps.py
Test the behavior of custom square root function, f_1, f_2, and f_3.

To run:
poetry run pytest tests/test_component_maps.py
Add the -s flag in order to see outputs
'''

import math
import cmath
import pytest
import numpy as np
from zippy.point import Point
from zippy.f_a import F_a

REL_TOL = 1e-9

def test_f1_branch_sign_positive():
    '''
    Ensure that, after f_1, the branch sign is assigned correctly
    to a point that lands on the right of the imaginary axis.
    '''
    a = Point(complex(1, 1), name='a')
    f = F_a(a)
    pt = Point(complex(.1, .1))
    result = f.f1(pt)
    assert result.branch_sign == 1

def test_f1_branch_sign_negative():
    '''
    Ensure that, after f_1, the branch sign is assigned correctly
    to a point that lands on the left of the imaginary axis.
    '''
    a = Point(complex(1, 1), name='a')
    f = F_a(a)
    pt = Point(complex(-.1, .1))
    result = f.f1(pt)
    assert result.branch_sign == -1

def test_f1_correct_computation():
    '''
    For a few representative points, ensure that f_1 actually performs
    the desired computation.
    '''

    # Will test for four points
    pts = [Point(complex(.5, .5)), Point(complex(-.5, -.5)), Point(complex(0, 3)), Point(complex(3, 0))]

    a = Point(complex(3, 4), name='a')
    b = 25 / 3 # \frac{\vert a \vert^2}{\real{a}}
    c = 25 / 4 # \frac{\vert a \vert^2}{\imag{a}}
    f = F_a(a)

    # Check both the real and imaginary component for each point
    for p in pts:
        assert math.isclose(f.f1(p).z.real, (p.z / (1 - (p.z/b))).real, rel_tol=REL_TOL)
        assert math.isclose(f.f1(p).z.imag, (p.z / (1 - (p.z/b))).imag, rel_tol=REL_TOL)

def test_f1_special_points():
    '''
    Ensures that the origin, a, and b are appropriately handled.
    '''
    a = Point(complex(3, 4), name='a')
    o = Point(complex(0, 0), name='o')
    b = Point(complex(25 / 3, 0), name='b')
    c = Point(complex(25 / 4, 0), name='c')             # FIXME: Do we want to add a test to ensure c is handled correctly?
    f = F_a(a)

    # a -> ic
    assert math.isclose(f.f1(a).z.real, 0)  
    assert math.isclose(f.f1(a).z.imag, 25 / 4) 

    # 0 -> 0
    assert math.isclose(f.f1(o).z.real, complex(0, 0).real)  
    assert math.isclose(f.f1(o).z.imag, complex(0, 0).imag)  

    # b -> \infty FIXME: How do we want to handle this? See F_a.f1 implementation  
    # See the definition of complex infinity:   
    # https://phys.libretexts.org/Bookshelves/Mathematical_Physics_and_Pedagogy/Complex_Methods_for_the_Sciences_(Chong)/08%3A_Branch_Points_and_Branch_Cuts/8.03%3A_Aside-_The_Meaning_of_Infinity_for_Complex_Numbers  
    assert math.isclose(np.abs(f.f1(b).z), np.inf)                

def test_f2_correct_computation():
    '''
    For a few representative points, ensure that f_2 actually performs
    the desired computaiton.
    '''

    pts = [Point(complex(0, 0))]