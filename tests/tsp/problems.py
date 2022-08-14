import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TSP:
    energy: float
    name: str = ""
    distances: np.ndarray = np.eye(1)
    root: Optional[int] = None
    circular: bool = False
    solutions: List[np.ndarray] = field(default_factory=list)

    def valid_solution(self, s):
        s = np.asarray(s)
        if s.ndim == 2:
            return all(self.valid_solution(sn) for sn in s)
        for valids in self.solutions:
            if np.all(valids == s):
                return True
        return False

    def __str__(self):
        return self.name


# Simple problem, three nodes, only one solution
simple_problem_open = TSP(
    name="Simple 3 node, reversible, open graph",
    distances=[[0.0, 1.0, 2.0], [1.0, 0.0, 3.0], [2.0, 3.0, 0.0]],
    circular=False,
    solutions=[[0, 1, 2], [2, 1, 0]],
    energy=3.0,
)

simple_problem = TSP(
    name="Simple 3 node, reversible, closed path",
    distances=[[0.0, 1.0, 2.0], [1.0, 0.0, 3.0], [2.0, 3.0, 0.0]],
    circular=True,
    solutions=[[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]],
    energy=6.0,
)


TSP_problems = [simple_problem]
