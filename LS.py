import QR
import LA


def backsub(matrix_a: list[list], vector_a: list) -> list:
    """Computes the solution vector of the input upper triangular 
    matrix and the input vector

    First, we set our result to equal the negative second element
    of vector_a multiplied by the difference of 1 over the negative 
    second element and the negative second matrix_a. For each
    element in the range of the length of matrix_a minus 2, minus 1,
    and minus 1, set a scalar equal to vector_a. For each index in the
    range in the length of the result, set the scalar minus each element of 
    the length of matrix_a mius 1 minus the index of matrix_a multiplied
    by the index of the result equal to the scalar. Then, set the scalar
    multiplied by the difference of 1 over the element and element of
    matrix_a equal to the scalar. Append the scalar to the result. Return
    the desired result and use [: : -1] to switch the vector.

    Args:
        matrix_a: An upper triangular matrix stored as a list of lists.
        vector_a: A vector stored as a list

    Returns:
        The soltuion vector
    """
    result: list = [vector_a[-1]*(1/(matrix_a[-1][-1]))]
    for element in range(len(matrix_a) - 2, -1, -1):
        scal: float = vector_a[element]
        for index in range(len(result)):
            scal -= matrix_a[len(matrix_a)-1-index][element]*result[index]
        scal *= 1/(matrix_a[element][element])
        result.append(scal)
    return result[: : -1]


def least_squares(matrix_a: list[list], vector_a: list) -> list:
    """Computes the least squares matrix of the input matrix and vector.

    First we set Q and R to teh householder version of matrix_a. Then,
    we set Q_1 equal to the conjugate transpose of Q. Set Q_2 equal to
    the mat_vec_multi of Q_1 and vector_a. Set the result equal to the
    backsub of R and Q_2. Return the desired result.

    Args: 
        matrix_a: A matrix stored as a list of lists.
        vector_a: A vector stored as a list.

    Returns:
        The least squares matrix
    """
    Q, R = QR.householder(matrix_a)
    Q_1 = QR.conjugate_transpose(Q)
    Q_2 = LA.mat_vec_multi(Q_1, vector_a)
    result = backsub(R, Q_2)
    return result