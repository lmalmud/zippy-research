'''
utils.py
Relevant math helper functions.
'''

import numpy as np

def sign(z: complex):
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
    
def f3sqrt(z: complex):
    '''
    Applies the square root function 
    sqrt(re^{i theta}) = r^{1/2}e^{i theta/2} to z
    where the branch cut is along (0, \infty) - which
    means that the argument of the outputs will lie between
    [0, 2\pi]
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
