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
    r = credentials.post('qubo_mc',
                         json = {
                             'matrix': validate_QUBO_matrix(matrix, 2048).tolist(),
                             'shots': validate.integer(shots, 1, 500)
                         })
    return r['solution'], r['cost']

def solve_QUBO_cont(matrix, shots=300, credentials=default_credentials):
    r = credentials.post('qubo_cont',
                         json = {
                             'matrix': validate_QUBO_matrix(matrix, 2048).tolist(),
                             'shots': validate.integer(shots, 0, 8192)
                         })
    return r['solution'], r['cost']

def solve_QUBO_bf(matrix, credentials=default_credentials):
    r = credentials.post('qubo_bf',
                         json = {
                             'matrix': validate_QUBO_matrix(matrix, 2**12).tolist()
                         })
    return r['solution'], r['cost']
