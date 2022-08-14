import inspirationq.qudo
import numpy as np
import unittest
from ..context import BaseAPITest
from .problems import simple_problem


class BaseQUDOTest(BaseAPITest):

    all_problems = [simple_problem]

    @classmethod
    def setUpClass(cls):
        if cls is BaseQUDOTest:
            raise unittest.SkipTest("Skip BaseQUDOTests, it's a base class")
        super(BaseQUDOTest, cls).setUpClass()

    def solve(self, problem):
        pass

    def test_solver(self):
        for problem in self.all_problems:
            s, E = self.solve(problem)
            self.assertTrue(problem.valid_solution(np.asarray(s)))
            self.assertTrue(E == problem.energy)


class TestQUDOMC(BaseQUDOTest):
    def solve(self, problem):
        return inspirationq.qudo.solve_QUDO_mc(
            problem.matrix, problem.vector, credentials=self.credentials
        )
