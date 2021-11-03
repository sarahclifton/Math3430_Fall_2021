import QR
import HW06
import pytest

matrix_01 = ([[1, 0, 1], [2, 1, 0]])
matrix_02 = [[1, 0], [-5, -5]]


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
    assert HW06.orthonormalize(matrix_01) == [[0.7071067811865475, 0, 0.7071067811865475], 
                                                    [0.577350269189626, 0.5773502691896258, -0.5773502691896257]]
    assert HW06.orthonormalize(matrix_02) == [[1, 0], [0, -1]]
