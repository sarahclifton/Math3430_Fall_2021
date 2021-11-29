import QR
import pytest


matrix_01 = [[1, 0, 1], [2, 1, 0]]
matrix_02 = [[1, 0], [-5, -5]]
matrix_03 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
scalar_01 = 2 + 3j
scalar_02 = 3 - 4j
scalar_03 = -2
scalar_04 = 2
scalar_05 = 3
vector_01 = [1, 0]
vector_02 = [0, 3]
vector_03 = [3, 3]
vector_04 = [1, 1]


def test_unstable_gram_schmidt():
    assert QR.unstable_gram_schmidt(matrix_01) == [[[0.7071067811865475, 0, 0.7071067811865475], 
                                                    [0.577350269189626, 0.5773502691896258, -0.5773502691896257]], 
                                                    [[1.4142135623730951, 0], [1.414213562373095, 1.7320508075688772]]]
    assert QR.unstable_gram_schmidt(matrix_02) == [[[1, 0], [0, -1]], [[1, 0], [-5, 5]]]

def test_stable_gram_schmidt():
    assert QR.stable_gram_schmidt(matrix_01) == [[[0.7071067811865475, 0.0, 0.7071067811865475], 
                                                    [0.577350269189626, 0.5773502691896258, -0.5773502691896257]], 
                                                    [[1.414213562373095, 0], [1.414213562373095, 1.7320508075688776]]]
    assert QR.stable_gram_schmidt(matrix_02) == [[[1, 0], [0, -1]], [[1, 0], [-5, 5]]]

def test_orthonormalize():
    assert QR.orthonormalize(matrix_01) == [[0.7071067811865475, 0, 0.7071067811865475], 
                                                    [0.577350269189626, 0.5773502691896258, -0.5773502691896257]]
    assert QR.orthonormalize(matrix_02) == [[1, 0], [0, -1]]

def test_conjugate():
    assert QR.conjugate(scalar_01) == 2 - 3j 
    assert QR.conjugate(scalar_02) == 3 + 4j

def test_conjugate_transpose():
    assert QR.conjugate_transpose(matrix_02) == [[1, -5], [0, -5]]
    assert QR.conjugate_transpose(matrix_03) == [[2, -2, 18], [2, 1, 0], [1, 2, 0]]

def test_deep_copy():
    assert QR.deep_copy(matrix_02) == [[1, 0], [-5, -5]]
    assert QR.deep_copy(matrix_03) == [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]

def test_sign():
    assert QR.sign(scalar_03) == -1
    assert QR.sign(scalar_04) == 1

def test_V_builder():
    assert QR.V_builder(vector_01) == [2, 0]
    assert QR.V_builder(vector_02) == [3, 3]

def test_identity():
    assert QR.identity(scalar_04) == [[1, 0], [0, 1]]
    assert QR.identity(scalar_05) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def test_vec_multi():
    assert QR.vec_multi(vector_01, vector_02) == [[0, 3], [0, 0]]
    assert QR.vec_multi(vector_03, vector_04) == [[3, 3], [3, 3]]

def test_F_builder():
    assert QR.F_builder(vector_01) == [[-1.0, 0.0], [0.0, 1.0]]
    assert QR.F_builder(vector_02) == [[1.0, 0.0], [0.0, -1.0]]

def test_Q_builder():
    assert QR.Q_builder(matrix_02, scalar_03) == [[1.0, 0.0], [0.0, 1.0]]
    assert QR.Q_builder(matrix_03, scalar_03) == [[0.6666666666666666, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

def test_householder():
    assert QR.householder(matrix_03) == [[[-0.6666666666666667, -0.6666666666666666, -0.3333333333333333], 
                                        [0.6666666666666667, -0.3333333333333334, -0.6666666666666667], 
                                        [-0.33333333333333337, 0.6666666666666667, -0.6666666666666666]], 
                                        [[-3.0000000000000004, -1.1657341758564147e-16, 1.5543122344752193e-16], 
                                        [2.220446049250313e-16, -3.0, 0.0], 
                                        [-12.000000000000002, 12.000000000000002, -6.000000000000002]]]
    assert QR.householder(matrix_02) == [[[-1, 0], [0, -1]], [[-1, 0], [5, 5]]]