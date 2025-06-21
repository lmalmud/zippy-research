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
from zippy.utils import f3sqrt

REL_TOL = 1e-9

def test_f3sqrt():
    '''
    Tests the custon-designed square root function with a branch cut
    along (0, \infty)
    '''

    # FIXME: I do not understand how this map is *supposed to* work.

    # -4 + 0i = 4e^{i\pi}
    # sqrt(-4 + 0i) = 2e^{.5i\pi}
    # assert f3sqrt(complex(-4, 0)).real == -2
    # assert math.isclose(f3sqrt(complex(-4, 0)).imag, .5 * np.pi, rel_tol = REL_TOL)

    # assert f3sqrt(complex(4, 0)).real == 2
    # assert math.isclose(f3sqrt(complex(4, 0)).imag, 0, rel_tol = REL_TOL)

    pass

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
    pts = [Point(complex(.5, .5)), Point(complex(-.5, -.5)), Point(complex(0, 3)), Point(complex(3, 0), on_axis = True)]

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
    b = 25/3
    # FIXME: Do we want to add a test to ensure c is handled correctly?
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
    assert math.isclose(np.abs(f.f1(Point(z=b)).z), np.inf)                

def test_f2_correct_computation():
    '''
    For a few representative points, ensure that f_2 actually performs
    the desired computaiton.
    '''
    a = Point(complex(3, 4), name='a')
    b = 25 / 3
    c = 25 / 4 
    f = F_a(a)

    pts = [Point(complex(1, 2)), Point(complex(-1, 2)), Point(complex(-3, 4))]
    for p in pts:
        assert f.f2(p).z.real == (p.z ** 2 + c **2).real
        assert f.f2(p).z.imag == (p.z ** 2 + c **2).imag

def test_f2_special_points():
    '''
    Ensure that where a and the origin are sent *after* f_1 are handled
    appropriately.
    '''
    a = Point(complex(3, 4), name='a')
    c = 25/4
    f = F_a(a)

    # 0 -> c^2
    # f_2(f_1(0)) = f_2(0) = c^2
    assert f.f2(Point(complex(0, 0), is_origin = True, on_axis= True)).z.real == (c ** 2)
    assert f.f2(Point(complex(0, 0), is_origin = True, on_axis= True)).z.imag == 0

    # ic -> 0
    assert f.f2(Point(complex(0, c), on_axis= True)).z.real == 0
    assert f.f2(Point(complex(0, c), on_axis= True)).z.imag == 0

def test_f3_correct_computation():
    '''
    Ensure that the computation of f_3 is correct for points
    partiularly assigned on the branch cut and with preassigned
    branches.
    '''
    a = Point(complex(3, 4), name='a')
    b = 25 / 3
    c = 25 / 4
    f = F_a(a)

    # A point that is on the real axis should be multivalued.
    point_on_branch = Point(complex(4, 0), on_arc = True, on_axis = True)
    results = f.f3(point_on_branch)

    assert len(results) == 2
    for result in results:
        assert result.z.real == 2 * result.branch_sign
        assert math.isclose(result.z.imag, 0, rel_tol=REL_TOL)

    # We would like a point that is initially on the positive real axis to be assigned the appropriate branch.
    point_on_axis_positive = Point(complex(4, 0), on_axis = True, branch_sign = 1)
    assert f.f3(point_on_axis_positive)[0].z.real == 2
    assert f.f3(point_on_axis_positive)[0].z.imag == 0

    # Similarly, a point that is initially on the negative real axis to stay there
    point_on_axis_negative = Point(complex(-4, 0), on_axis = True, branch_sign = -1)
    assert f.f3(point_on_axis_negative)[0].z.real == -2
    assert f.f3(point_on_axis_negative)[0].z.imag == 0

def test_f3_special_points():
    pass