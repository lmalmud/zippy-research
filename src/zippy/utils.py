'''
utils.py
Relevant math helper functions.
'''

import numpy as np
import colorsys
from zippy.point import Point
from typing import List

def sign(z: complex) -> int:
    '''
    Returns 1 if the real part is greater than or equal to
    zero and -1 otherwise.
    Note that the imaginary axis is included as "positive."
    Parameters:
    z (complex): the input point
    Returns:
    int
    '''
    if z.real >= 0:
        return 1
    else:
        return -1
    
def f3sqrt(z: complex) -> complex:
    '''
    Applies the square root function 
    sqrt(re^{i theta}) = r^{1/2}e^{i theta/2} to z
    where the branch cut is along (0, \infty) - which
    means that the argument of the outputs will lie between
    [0, 2\pi]
    This code was taken from: https://flothesof.github.io/branch-cuts-with-square-roots.html
    Parameters:
    z (complex): point to apply map to
    Returns:
    complex: sqrt(z)
    '''

    # np.angle = tangent function for complex inputs
    argument = np.angle(z)
    modulus = np.abs(z)

    # Shift over 2 * np.pi, which defines the branch cut
    argument = np.mod(argument + 2 * np.pi, 2 * np.pi) - 2 * np.pi
    
    return np.sqrt(modulus) * np.exp(1j * argument / 2)

def get_color(z: complex) -> List:
    '''
    Returns the color associated with the point at this particular location.
    Note that this does not update the color.

    https://en.wikipedia.org/wiki/Domain_coloring

    Parameters:
    z (complex): the point to assign a color to
    Returns:
    List: (r, g, b, a)
    '''

    r = z.real
    i = z.imag
    h = np.arctan2(r, i) + (2 * np.pi / 3)
    h = h / (np.pi * 2)
    s = 1
    r = np.sqrt(r ** 2 + i ** 2)
    l = (2 / np.pi) * np.arctan(r)
    return colorsys.hls_to_rgb(h, l, s)

def generate_complex(min_r: float, max_r: float, min_c: float, max_c: float, density=10) -> List[complex]:
    '''
    Generates a list of points in the complex plane with
    real value in the range [min_r, max_r] and complex value
    in the range [min_c, max_c].
    Parameters:
    min_r (float), min_c (float): the minimum value for real and complex components, respectively
    max_r (flaot), max_c (float): the maximum value for real and complex components, respectively
    density (int): the number of points generated per unit
    Returns:
    List[complex]: list of complex values in the given range with specified density
    '''
    reals = np.linspace(min_r, max_r, density*(max_r - min_r))
    imags = np.linspace(min_c, max_c, density*(max_c - min_c))
    results = []
    for r in reals:
        for i in imags:
            results.append(complex(r, i))
    return results

def generate_complex_point(min_r: float, max_r: float, min_c: float, max_c: float, density=10) -> List[Point]:
    '''
    Generates a list of Point objects
    real value in the range [min_r, max_r] and complex value
    in the range [min_c, max_c].
    Parameters:
    min_r (float), min_c (float): the minimum value for real and complex components, respectively
    max_r (flaot), max_c (float): the maximum value for real and complex components, respectively
    density (int): the number of points generated per unit
    Returns:
    List[Point]: list of Points in the given range with specified density
    '''
    reals = np.linspace(min_r, max_r, density*(max_r - min_r))
    imags = np.linspace(min_c, max_c, density*(max_c - min_c))
    return [Point(complex(r, i)) for r in reals for i in imags]

def get_coords_from_complex(lst: List[complex]) -> List[float]:
    '''
    Given a list of complex points, returns a list of order pairs of
    real and imaginary parts.
    Parameters:
    lst (List[complex]): the list of points to be translated into their components
    Returns:
    List[float]
    '''
    results = []
    for item in lst:
        results.append([item.real, item.complex])
    return results

def get_real_image_from_complex(lst: List[complex]):
    '''
    Given a list of complex points, returns two lists:
    one with the real components and one with the corresponding
    imaginary components.
    Parameters:
    lst (List[complex]): the list of points to be translated into their components
    Returns:
    List[float]: real components
    List[float]: imaginary components
    '''
    reals = []
    imags = []
    for p in lst:
        reals.append(p.real)
        imags.append(p.imag)
    return reals, imags

def graph_complex(pts: List[complex], ax, func):
    '''
    Plots the complex function on the given axis.
    Parameters:
    pts (List[complex]): list of points to apply the function to
    ax (matplotlib axis object): to show the graph on
    func (function): function to apply to points
    '''
    pass