import numpy as np
from .api.credentials import default_credentials
from .api import validate

def validate_QUBO_matrix(matrix, max_dimension):
    matrix = np.array(matrix)
    if matrix.ndim != 2 or \
       matrix.shape[0] != matrix.shape[1] or \
       matrix.shape[0] > max_dimension:
        raise Exception('Not a valid QUBO matrix')
    return matrix

def solve_QUBO_mc(matrix, shots=300, credentials=default_credentials):
    """Solve a QUBO problem by stochastic optimization.
    
    :param matrix: Real, square matrix for the QUBO problem.
    :type matrix: numpy.ndarray or similar
    :param shots: Number of stochastic trajectories to explore (between 1 and 500)
    :type shots: int
    :returns:
        - s - vector of binary values, solution of the problem
        - E - minimum value of the QUBO cost function
    """
    r = credentials.post('qubo_mc',
                         json = {
                             'matrix': validate_QUBO_matrix(matrix, 2048).tolist(),
                             'shots': validate.integer(shots, 1, 500)
                         })
    return r['solution'], r['cost']

def solve_QUBO_cont(matrix, shots=300, credentials=default_credentials):
    """Solve a QUBO problem by quantum-inspired spin-vector Monte Carlo.

    The algorithm is based on the annealing of quantum states under the constraint
    of no entanglement, combined with stochastic sampling over a number of :code:`shots`.
    
    :param matrix: Real, square matrix for the QUBO problem.
    :type matrix: numpy.ndarray or similar
    :param shots: Number of stochastic trajectories to explore (between 1 and 8192)
    :type shots: int
    :returns:
        - s - vector of binary values, solution of the problem
        - E - minimum value of the QUBO cost function
    """
    r = credentials.post('qubo_cont',
                         json = {
                             'matrix': validate_QUBO_matrix(matrix, 2048).tolist(),
                             'shots': validate.integer(shots, 0, 8192)
                         })
    return r['solution'], r['cost']

def solve_QUBO_bf(matrix, credentials=default_credentials):
    """Solve a QUBO problem by brute force exploration of all possible combinations.

    .. warning::
    
        The resources for this exhaustive exploration grow exponentially with
        the problem size. The classical backend will raise an exception for
        problems involving 31 bits or more.
    
    :param matrix: Real, square matrix for the QUBO problem.
    :type matrix: numpy.ndarray or similar
    :returns:
        - s - vector of binary values, solution of the problem
        - E - minimum value of the QUBO cost function
    """
    r = credentials.post('qubo_bf',
                         json = {
                             'matrix': validate_QUBO_matrix(matrix, 2**12).tolist()
                         })
    return r['solution'], r['cost']
