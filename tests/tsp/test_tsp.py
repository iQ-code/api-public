import inspirationq.tsp
import numpy as np
from ..context import BaseAPITest
from .problems import simple_problem


class TestTSPMC(BaseAPITest):

    all_problems = [simple_problem]

    def solve(self, problem):
        return inspirationq.tsp.solve_TSP_mc(
            problem.distances, circular=problem.circular, credentials=self.credentials
        )

    def test_solver(self):
        for problem in self.all_problems:
            s, E = self.solve(problem)
            self.assertTrue(problem.valid_solution(np.asarray(s)))
            self.assertTrue(E == problem.energy)

