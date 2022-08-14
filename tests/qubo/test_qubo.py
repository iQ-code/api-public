import inspirationq.qubo
import numpy as np
import unittest
from ..context import BaseAPITest
from .problems import simple_problem


class BaseQUBOTest(BaseAPITest):

    all_problems = [simple_problem]

    @classmethod
    def setUpClass(cls):
        if cls is BaseQUBOTest:
            raise unittest.SkipTest("Skip BaseQUBOTests, it's a base class")
        super(BaseQUBOTest, cls).setUpClass()

    def solve(self, problem):
        pass

    def test_solver(self):
        for problem in self.all_problems:
            s, E = self.solve(problem)
            self.assertTrue(problem.valid_solution(np.asarray(s)))
            self.assertTrue(E == problem.energy)


class TestQUBOBruteForce(BaseQUBOTest):
    def solve(self, problem):
        return inspirationq.qubo.solve_QUBO_cont(
            problem.matrix, credentials=self.credentials
        )


class TestQUBOMC(BaseQUBOTest):
    def solve(self, problem):
        return inspirationq.qubo.solve_QUBO_mc(
            problem.matrix, credentials=self.credentials
        )
