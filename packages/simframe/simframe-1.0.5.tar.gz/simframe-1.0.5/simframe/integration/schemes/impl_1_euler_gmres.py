from simframe.integration.scheme import Scheme

import numpy as np
from scipy.sparse import linalg


def _f_impl_1_euler_gmres(x0, Y0, dx, jac=None, gmres_opt={"atol": 0.}, *args, **kwargs):
    """Implicit 1st-order Euler integration scheme with GMRES solver

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
    gmres_opt : dict, optional, default : {"atol": 0.}
        dictionary with options for scipy GMRES solver
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

    A = eye - dx*jac
    b = Y0[None] if Y0.shape == () else Y0
    res, state = linalg.gmres(A, b, **gmres_opt)
    if state != 0:
        return False
    else:
        return res - Y0


class impl_1_euler_gmres(Scheme):
    """Class for implicit 1st-order Euler method with GMRES solver"""

    def __init__(self, *args, **kwargs):
        super().__init__(_f_impl_1_euler_gmres,
                         description="Implicit 1st-order Euler method with GMRES solver", *args, **kwargs)
