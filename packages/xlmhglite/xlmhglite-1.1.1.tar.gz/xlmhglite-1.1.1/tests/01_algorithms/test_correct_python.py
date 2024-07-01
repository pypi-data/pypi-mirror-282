# Copyright (c) 2016-2019 Florian Wagner
#
# This file is part of XL-mHG.

"""Tests for the Python implementation of the XL-mHG test."""

import itertools as it

import numpy as np
import pytest
from scipy.stats import hypergeom

from xlmhglite import mhg


def get_xlmhg_stat_slow(v, X, L, tol=1e-12):
    # calculate the XL-mHG test statistic (inefficient)

    # type checking
    assert isinstance(v, np.ndarray)
    assert v.dtype == np.uint8
    assert isinstance(X, int)
    assert isinstance(L, int)

    # check if values are valid
    N = v.size
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
            if hgp < stat or mhg.is_equal(hgp, stat, tol):
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
    C = np.int64(list(it.combinations(range(N), K)))
    p = C.shape[0]
    np.random.seed(seed)
    for i in range(num_lists):
        idx = np.random.randint(p)
        v = np.zeros(N, dtype=np.uint8)
        v[C[idx, :]] = 1
        indices = C[idx, :]
        stat, n_star = mhg.get_xlmhg_stat(indices, N, K, X, L)
        stat_ref, n_star_ref = get_xlmhg_stat_slow(v, X, L)
        assert mhg.is_equal(stat, stat_ref, tol=tol) and \
               n_star == n_star_ref, repr(v)


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
            stat, n_star = mhg.get_xlmhg_stat(indices, N, K, X, L)
            stat_ref, n_star_ref = get_xlmhg_stat_slow(v, X, L)
            assert mhg.is_equal(stat, stat_ref, tol=tol) and \
                   n_star == n_star_ref, repr(v)


def test_alg1_alg2_accuracy_difference():
    a = 20
    bvals = np.arange(50, 100, dtype=np.int64)
    tol = 1e-12

    k = bvals.size
    truth = np.zeros(k, dtype=np.float64)
    pval1 = np.zeros(k, dtype=np.float64)
    pval2 = np.zeros(k, dtype=np.float64)
    for i, b in enumerate(bvals):
        b = int(b)
        N = a + b
        K = a
        X = 1
        L = N
        n = a
        k = K
        truth[i] = hypergeom.pmf(k, N, K, n)

        v = np.r_[np.ones(a, dtype=np.uint8), np.zeros(b, dtype=np.uint8)]
        indices = np.uint16(np.nonzero(v)[0])

        stat, n_star = mhg.get_xlmhg_stat(indices, N, K, X, L)
        p1 = mhg.get_xlmhg_pval1(N, K, X, L, stat)
        p2 = mhg.get_xlmhg_pval2(N, K, X, L, stat)
        pval1[i] = p1
        pval2[i] = p2

    assert np.all(~np.isnan(pval2))
    assert np.any(np.isnan(pval1))
    for i in range(bvals.size):
        assert mhg.is_equal(pval2[i], truth[i], tol=tol)


def test_mhg_pval_cross():
    # test if mHG p-value is correct
    # by comparing output of Algorithms 1 and 2 to each other
    # for random lists with N = 20 and K = 5
    tol = 1e-11
    seed = 123456789
    num_lists = 500

    N = 20
    K = 5
    X = 1
    L = N
    C = np.int64(list(it.combinations(range(N), K)))
    p = C.shape[0]
    np.random.seed(seed)
    for i in range(num_lists):
        idx = np.random.randint(p)
        v = np.zeros(N, dtype=np.uint8)
        v[C[idx, :]] = 1
        indices = np.uint16(np.nonzero(v)[0])
        stat, n_star = mhg.get_xlmhg_stat(indices, N, K, X, L)
        pval1 = mhg.get_xlmhg_pval1(N, K, X, L, stat)
        pval2 = mhg.get_xlmhg_pval2(N, K, X, L, stat)
        assert mhg.is_equal(pval1, pval2, tol=tol), repr(v)


def test_xlmhg_pval_cross():
    # - test if XL-mHG p-value is correct,
    #   by comparing output of Algorithms 1 and 2 to each other
    # - goes over a particular example vector, for all combinations
    #   of X and L
    v = np.uint8([1, 0, 1, 1, 0, 1] + [0] * 12 + [1, 0])  # example from paper
    N = v.size
    K = int(np.sum(v != 0))
    indices = np.uint16(np.nonzero(v)[0])
    tol = 1e-11
    assert N == 20 and K == 5
    for L in range(1, N + 1):
        for X in range(1, N + 1):
            stat, n_star = mhg.get_xlmhg_stat(indices, N, K, X, L)
            pval1 = mhg.get_xlmhg_pval1(N, K, X, L, stat)
            pval2 = mhg.get_xlmhg_pval2(N, K, X, L, stat)
            assert mhg.is_equal(pval1, pval2, tol=tol), repr(v)


def test_invalid():
    v = np.uint8([1, 0, 1, 1, 0, 1] + [0] * 12 + [1, 0])  # example from paper
    N = v.size
    int(np.sum(v != 0))
    X = 1
    L = N
    K = int(np.sum(v != 0))
    indices = np.uint16(np.nonzero(v)[0])

    tol = 1e-11
    with pytest.raises(ValueError):
        other = np.uint8([])
        stat, cutoff = mhg.get_xlmhg_stat(other, 0, 0, X, L, tol)
    with pytest.raises(ValueError):
        stat, cutoff = mhg.get_xlmhg_stat(indices, N, K, -1, L, tol)
    with pytest.raises(ValueError):
        stat, cutoff = mhg.get_xlmhg_stat(indices, N, K, X, -1, tol)
    with pytest.raises(ValueError):
        stat, cutoff = mhg.get_xlmhg_stat(indices, N, K, X, L, -1.0)
