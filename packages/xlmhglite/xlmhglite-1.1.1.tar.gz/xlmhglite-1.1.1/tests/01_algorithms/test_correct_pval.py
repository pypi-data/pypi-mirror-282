# Copyright (c) 2016-2019 Florian Wagner
#
# This file is part of XL-mHG.

"""Tests for the Cython implementations of the XL-mHG p-value.."""

import numpy as np
from scipy.stats import hypergeom

from xlmhglite import mhg, mhg_cython

def test_cross():
    """Compares p-values calculated using PVAL1 and PVAL2."""
    N = 50
    K = 10

    #tol = 1e-11
    tol = 5e-6

    W = N-K
    table = np.empty((K+1, W+1), dtype=np.longdouble)

    # calculate hypergeometric p-values for all configurations
    configs = np.ones((K+1, W+1), dtype=np.float64)
    for k in range(1, K+1):
        for w in range(W):
            n = k+w
            configs[k, w] = hypergeom.sf(k-1, N, K, n)

    tests = 0
    for X in range(1, N+1):
        for L in range(N, 0, -1):
            # calculate all possible XL-mHG test statistics
            S = np.ones((K+1, W+1), dtype=np.float64)
            for n in range(L+1):
                k = min(K, n)
                w = n-k
                while k >= X and w <= W and n <= L:
                    S[k, w] = configs[k, w]
                    k -= 1
                    w += 1

            all_stat = np.sort(np.unique(S.ravel()))[::-1]

            for stat in all_stat:
                pval1 = mhg_cython.get_xlmhg_pval1(N, K, X, L, stat, table)
                pval2 = mhg_cython.get_xlmhg_pval2(N, K, X, L, stat, table)
                tests += 1
                assert mhg.is_equal(pval1, pval2, tol=tol)

    print('Calculated %d bounds, based on %d configurations.'
          %(tests, configs.size))
