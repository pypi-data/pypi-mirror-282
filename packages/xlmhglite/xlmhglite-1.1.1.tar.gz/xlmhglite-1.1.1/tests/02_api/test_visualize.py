# Copyright (c) 2016-2019 Florian Wagner
#
# This file is part of XL-mHG.

"""Tests the visualizing function of the Python API (`get_result_figure`)."""

import os

import pytest
import numpy as np
from plotly.offline import plot

import xlmhglite

def test_figure(tmpdir):

    v = np.uint8([1,0,1,1,0,1] + [0]*12 + [1,0])
    X = 3
    L = 10

    N = v.size
    indices = np.uint16(np.nonzero(v)[0])

    result = xlmhglite.get_xlmhg_test_result(N, indices, X=X, L=L)

    fig = xlmhglite.get_result_figure(result)
    output_file = str(tmpdir.join('plot1.html'))
    plot(fig, filename=output_file, auto_open=False)
    assert os.path.isfile(output_file)

    fig = xlmhglite.get_result_figure(result, width=500, height=350)
    output_file = str(tmpdir.join('plot2.html'))
    plot(fig, filename=output_file, auto_open=False)
    assert os.path.isfile(output_file)

    fig = xlmhglite.get_result_figure(result, show_title=True, show_inset=False)
    output_file = str(tmpdir.join('plot3.html'))
    plot(fig, filename=output_file, auto_open=False)
    assert os.path.isfile(output_file)


def test_figure_double_axis(tmpdir):

    v = np.uint8([1,0,1,1,0,1] + [0]*12 + [1,0])
    X = 3
    L = 10

    N = v.size
    indices = np.uint16(np.nonzero(v)[0])

    result = xlmhglite.get_xlmhg_test_result(N, indices, X=X, L=L)

    fig = xlmhglite.get_result_figure(result, plot_fold_enrichment=True)
    output_file = str(tmpdir.join('plot4.html'))
    plot(fig, filename=output_file, auto_open=False)
    assert os.path.isfile(output_file)