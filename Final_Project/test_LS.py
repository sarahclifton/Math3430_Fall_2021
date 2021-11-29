import LS
import pytest

matrix_01 = [[1, 2, 3], [1, 1, 2], [2, 1, 2]]
vector_01 = [3, 3, 1]
matrix_02 = [[2, 0, 0], [1, 3, 0], [2, 4, 5]]
vector_02 = [1, 2, 3]

def test_backsub():
    assert LS.backsub(matrix_01, vector_01) == [-0.5, 2.5, 0.5]
    assert LS.backsub(matrix_02, vector_02) == [-0.03333333333333337, -0.13333333333333344, 0.6000000000000001]

def test_least_squares():
    assert LS.least_squares(matrix_01, vector_01) == [5.0, -12.000000000000005, 5.000000000000004]
    assert LS.least_squares(matrix_02, vector_02) == [-0.03333333333333337, -0.13333333333333344, 0.6000000000000001]