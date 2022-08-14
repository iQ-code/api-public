import numpy as np
from .api.credentials import default_credentials
from .api import validate


def validate_TSP_matrix(matrix, max_dimension):
    matrix = np.asarray(matrix)
    if (
        matrix.ndim != 2
        or matrix.shape[0] != matrix.shape[1]
        or matrix.shape[0] > max_dimension
    ):
        raise Exception("Not a valid TSP matrix")
    return matrix.tolist()


def solve_TSP_mc(
    distances, steps=2000, shots=300, circular=False, credentials=default_credentials,
):
    """Solve a QUDO problem by stochastic optimization.
    
    :param distances: Real, square matrix for the QUDO problem.
    :type distances: numpy.ndarray or similar
    :param steps: Depth of each stochastic trajectory (between 1 and 10000)
    :type steps: int
    :param shots: Number of stochastic trajectories to explore (between 1 and 500)
    :type shots: int
    :param circular: Whether the route ends at the starting point
    :type circular: boolean
    :returns:
        - s - vector of integer values, solution of the problem
        - E - value of the distance associated to the solution
    """
    r = credentials.post(
        "tsp_mc",
        json={
            "distances": validate_TSP_matrix(distances, 2048),
            "steps": validate.integer(steps, 1, 10000),
            "shots": validate.integer(shots, 1, 500),
            "circular": validate.boolean(shots),
        },
    )
    return r["solution"], r["cost"]
