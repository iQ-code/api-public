import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class QUBO:
    energy: float
    name: str = ""
    matrix: np.ndarray = np.ones(1)
    solutions: List[np.ndarray] = field(default_factory=list)

    def valid_solution(self, s):
        if s.ndim == 2:
            return all(self.valid_solution(sn) for sn in s)
        for valids in self.solutions:
            if np.all(valids == s):
                return True
        return False

    def __str__(self):
        return self.name


# Simple problem, two qubits, only one solution
simple_problem = QUBO(
    name="Simple 2 qubit problem",
    matrix=[[1.0, 0.0], [0.0, -1.0]],
    solutions=[[0, 1]],
    energy=-1.0,
)

# Simple problem, two qubits, three solutions with the same cost
degenerate_problem = QUBO(
    name="Degenerate 2 qubit problem",
    matrix=[[0.0, 1.0], [1.0, 0.0]],
    solutions=[[0, 0], [1, 0], [0, 1]],
    energy=0.0,
)


class Aligned(QUBO):
    def __init__(self, size, sign):
        super().__init__(
            name=f"Aligned {size} bits",
            matrix=np.eye(size) * sign,
            solutions=[np.zeros(size) if sign > 0 else np.ones(size)],
            energy=-size if sign < 0 else 0,
        )


class RandomField(QUBO):
    def __init__(self, size, seed=None):
        h = np.random.default_rng(seed).normal(size=(size,))
        super().__init__(
            name=f"Random field {h}",
            matrix=np.diag(h),
            solutions=[(h < 0).astype(int)],
            energy=np.sum(h[h < 0]),
        )


class Ferromagnetic1D(QUBO):
    def __init__(self, size):
        super().__init__(
            name=f"Ferromagneti1D {size}",
            matrix=np.diag(np.ones(size - 1), 1),
            energy=size - 1,
        )

    def valid_solution(self, s):
        return np.all(s == s[0])

QUBO_problems = sum(
    [
        [Aligned(size, +1) for size in range(1, 20)],
        [Aligned(size, -1) for size in range(1, 20)],
        [RandomField(size, 13221097) for size in range(1, 20)],
        # [Ferromagnetic1D(size) for size in range(1,20)],
    ],
    [],
)

