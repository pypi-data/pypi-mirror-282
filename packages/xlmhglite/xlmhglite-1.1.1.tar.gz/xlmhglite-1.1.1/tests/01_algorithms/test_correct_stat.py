# Copyright (c) 2016-2019 Florian Wagner
#
# This file is part of XL-mHG.

"""Tests for the Cython implementation of the XL-mHG test statistic."""

import itertools as it

import numpy as np
from scipy.stats import hypergeom

from xlmhglite import mhg_cython
from xlmhglite.mhg import is_equal


def get_xlmhg_stat_slow(v, X=None, L=None, tol=1e-12):
    # calculate the XL-mHG test statistic (inefficient)

    # type checking
    assert isinstance(v, np.ndarray)
    assert v.dtype == np.uint8
    if X is not None:
        assert isinstance(X, int)
    if L is not None:
        assert isinstance(L, int)

    N = v.size
    if X is None:
        X = 1
    if L is None:
        L = N

    # check if values are valid
    if not (1 <= X <= N):
        raise ValueError('Invalid value X=%d; should be >= 1 and <= N.' % (X))
    if not (1 <= L <= N):
        raise ValueError('Invalid value L=%d; should be >= 1 and <= N.' % (L))

    K = int(np.sum(v != 0))
    if K == 0:
        # special case when K=0
        return 1.0, 0

    k = 0
    stat = 1.1
    n_star = 0
    for i in range(L):
        if v[i] != 0:
            k += 1
        if k >= X:
            hgp = hypergeom.sf(k - 1, N, K, i + 1)
            if hgp < stat or is_equal(hgp, stat, tol):
                stat = hgp
                n_star = i + 1

    stat = min(stat, 1.0)
    return stat, n_star


def test_mhg_stat():
    # test if mHG test statistic is correct
    # tests random lists with N = 20 and K = 5
    tol = 1e-11
    seed = 123456789
    num_lists = 500

    N = 20
    K = 5
    X = 1
    L = N
    C = np.uint16(list(it.combinations(range(N), K)))
    p = C.shape[0]
    np.random.seed(seed)
    for i in range(num_lists):
        idx = np.random.randint(p)
        indices = C[idx, :]
        v = np.zeros(N, dtype=np.uint8)
        v[indices] = 1
        # stat, n_star, _ = xlmhg_test(v, X, L)
        stat, n_star = mhg_cython.get_xlmhg_stat(indices, N, K, X, L)
        stat_ref, n_star_ref = get_xlmhg_stat_slow(v, X, L)
        assert is_equal(stat, stat_ref, tol=tol) and n_star == n_star_ref, \
            repr(v)


def test_xlmhg_stat():
    # test if XL-mHG test statistic is correct
    # uses a particular example vector,
    # and goes over all combinations of X and L
    v = np.uint8([1, 0, 1, 1, 0, 1] + [0] * 12 + [1, 0])  # example from paper
    indices = np.uint16(np.nonzero(v)[0])
    N = v.size
    K = indices.size
    tol = 1e-11

    assert N == 20 and K == 5
    for L in range(1, N + 1):
        for X in range(1, N + 1):
            stat, cutoff = mhg_cython.get_xlmhg_stat(indices, N, K, X, L)
            stat_ref, cutoff_ref = get_xlmhg_stat_slow(v, X, L)
            assert is_equal(stat, stat_ref, tol=tol) and \
                   cutoff == cutoff_ref, repr(v)
