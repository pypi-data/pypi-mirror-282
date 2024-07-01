from simframe.integration.scheme import Scheme

import numpy as np


def _f_impl_2_midpoint_direct(x0, Y0, dx, jac=None, *args, **kwargs):
    """Implicit 2nd-order midpoint method with direct matrix inversion

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
     1/2 | 1/2
    -----|-----
         |  1 
    """
    jac = Y0.jacobian(x0 + dx) if jac is None else jac  # Jacobain
    N = jac.shape[0] if jac.ndim else 1                 # Problem size
    eye = np.eye(N)                                     # Identity matrix

    A = eye - 0.5*dx*jac
    Ainv = np.linalg.inv(A)
    k1 = np.dot(Ainv, np.dot(jac, Y0))

    return dx*k1


class impl_2_midpoint_direct(Scheme):
    """Class for implicit 2nd-order direct midpoint method"""

    def __init__(self, *args, **kwargs):
        super().__init__(_f_impl_2_midpoint_direct,
                         description="Implicit 2nd-order direct midpoint method", *args, **kwargs)
