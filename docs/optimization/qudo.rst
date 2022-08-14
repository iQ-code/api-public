.. _optimization_qudo:

=====================================
Quadratic Integer Optimization (QUDO)
=====================================

A quadratic integerp optimization problem, or QUDO in abbreviated form, is the
problem of minimizing a degree-2 polynomial function of :math:`N` integer
:math:`x_1` to :math:`x_N`.

The most general QUDO problem for :math:`N` variables is defined by the linear 
and quadratic components of the cost function, given by a real vector
:math:`d` of size :code:`N` and a square real matrix :math:`Q` of size
:math:`N\times N`

.. math::

    E = \sum_{m,n=1}^N x_m Q_{mn} x_n + \sum_{m=1}^n d_n x_n

The library offers one solver.

.. autofunction:: inspirationq.qudo.solve_QUBO_mc


