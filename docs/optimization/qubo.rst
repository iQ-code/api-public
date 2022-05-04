.. _optimization_qubo:

====================================
Quadratic Binary Optimization (QUBO)
====================================

A quadratic binary optimization problem, or QUBO in abbreviated form, is the
problem of minimizing a degree-2 polynomial function of :math:`N` Bolean variables
:math:`s_1` to :math:`s_N` taking values :code:`0` or :code:`1`.

The most general QUBO problem for :math:`N` Boolean variables is completely
defined by a matrix of real coefficients :math:`Q`

.. math::

    E = \sum_{m,n=1}^N s_m Q_{mn} s_n

The library offers three solvers for this unconstrained problem.

.. autofunction:: inspirationq.qubo.solve_QUBO_bf

.. autofunction:: inspirationq.qubo.solve_QUBO_cont

.. autofunction:: inspirationq.qubo.solve_QUBO_mc
