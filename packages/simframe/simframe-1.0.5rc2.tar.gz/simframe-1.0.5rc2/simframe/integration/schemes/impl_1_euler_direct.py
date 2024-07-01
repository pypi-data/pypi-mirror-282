from simframe.integration.scheme import Scheme

import numpy as np


def _f_impl_1_euler_direct(x0, Y0, dx, jac=None, *args, **kwargs):
    """Implicit 1st-order Euler integration scheme with direct matrix inversion

    Parameters
    ----------
    x0 : Intvar
        Integration variable at beginning of scheme
    Y0 : Field
        Variable to be integrated at the beginning of scheme
    dx : IntVar
        Stepsize of integration variable
    jac : Field, optional, defaul : None
        Current Jacobian. Will be calculated, if not set
    args : additional positional arguments
    kwargs : additional keyworda arguments

    Returns
    -------
    dY : Field
        Delta of variable to be integrated

    Butcher tableau
    ---------------
     1 | 1
    ---|---
       | 1 
    """
    jac = Y0.jacobian(x0 + dx) if jac is None else jac  # Jacobain
    N = jac.shape[0] if jac.ndim else 1                 # Problem size
    eye = np.eye(N)                                     # Identity matrix

    A = eye - dx * jac
    return np.dot(np.linalg.inv(A)-eye, Y0)


class impl_1_euler_direct(Scheme):
    """Class for implicit 1st-order direct Euler method"""

    def __init__(self, *args, **kwargs):
        super().__init__(_f_impl_1_euler_direct,
                         description="Implicit 1st-order direct Euler method", *args, **kwargs)
