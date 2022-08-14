import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class QUDO:
    energy: float
    name: str = ""
    matrix: np.ndarray = np.ones(1)
    vector: np.ndarray = np.ones((1,))
    solutions: List[np.ndarray] = field(default_factory=list)

    def valid_solution(self, s):
        print(f"Solution:\n{s}")
        if s.ndim == 2:
            return all(self.valid_solution(sn) for sn in s)
        for valids in self.solutions:
            if np.all(valids == s):
                return True
        return False

    def __str__(self):
        return self.name


# Simple problem, two qubits, only one solution
simple_problem = QUDO(
    name="Simple 2 qubit problem",
    matrix=[[1.0, 0.0], [0.0, 1.0]],
    vector=[-2.0, -6.0],
    solutions=[[2, 6]],
    energy=-20.0,
)


QUDO_problems = [simple_problem]
