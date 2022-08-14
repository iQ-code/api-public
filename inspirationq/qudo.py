import numpy as np
from .api.credentials import default_credentials
from .api import validate


def validate_QUDO_matrix(matrix, max_dimension):
    matrix = np.asarray(matrix)
    if (
        matrix.ndim != 2
        or matrix.shape[0] != matrix.shape[1]
        or matrix.shape[0] > max_dimension
    ):
        raise Exception("Not a valid QUDO matrix")
    return matrix.tolist()


def validate_QUDO_vector(vector, max_dimension):
    if vector is not None:
        vector = np.asarray(vector)
        if vector.ndim != 1 or vector.shape[0] > max_dimension:
            raise Exception("Not a valid QUDO vector")
        vector = vector.tolist()
    return vector


def solve_QUDO_mc(
    matrix,
    vector=None,
    steps=2000,
    shots=300,
    min_n=None,
    max_n=None,
    credentials=default_credentials,
):
    """Solve a QUDO problem by stochastic optimization.
    
    :param matrix: Real, square matrix for the QUDO problem.
    :type matrix: numpy.ndarray or similar
    :param vector: Real vector for the QUDO problem
    :type vector: numpy.ndarray or similar, or None
    :param steps: Depth of each stochastic trajectory (between 1 and 10000)
    :type steps: int
    :param shots: Number of stochastic trajectories to explore (between 1 and 500)
    :type shots: int
    :param min_n: Vector of real values that lower-bound the solution
    :type min_n: numpy.ndarray or similar, or None
    :param max_n: Vector of real values that upper-bound the solution
    :type max_n: numpy.ndarray or similar, or None
    :returns:
        - s - vector of integer values, solution of the problem
        - E - minimum value of the QUDO cost function
    """
    r = credentials.post(
        "qudo_mc",
        json={
            "matrix": validate_QUDO_matrix(matrix, 2048),
            "vector": validate_QUDO_vector(vector, 2048),
            "min_n": validate_QUDO_vector(min_n, 2048),
            "max_n": validate_QUDO_vector(max_n, 2048),
            "steps": validate.integer(steps, 1, 10000),
            "shots": validate.integer(shots, 1, 500),
        },
    )
    return r["solution"], r["cost"]
