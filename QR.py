"""
This assignment is due by 11:59pm on 10/29/2021. 

For this assignment you will be writing a python script named QR.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a[outer_index] of the matrix. Use of any other
representation will result in an earned grade of 0.
"""

import LA

#1
"""
matrix_a function which implements the unstable version of Gram-Schmidt for reduced QR
factorization. It will take as it's argument a matrix and will return a list of 
two matrices. The first will be Q and the second will be R from the QR factorization 
described in the algorithm.
"""

def unstable_gram_schmidt(matrix_a: list[list]) -> list[list]: 
    """Computes QR factorization using the unstable Gram-Schmidt process. 

    Create an empty list for Q and a matrix of zeros for V and R. For each
    outer index, overwrite the outer index of V with the outer index of 
    matrix a. This will be the same length of matrix a. For every inner index 
    we have going from zero to the outer index, we will overwrite the outer 
    and inner indexes of R with inner product function of the inner index of 
    Q and the outer index of V. Then, we will overwrite a variable, s, with
    the scalar vector multiplication function of inner index of Q, and the
    negative outer and inner indexes of R. Next, we will overwrite the outer 
    index of V with the add vectors function of the outer index of V and s.
    Overwirte the outer indexes of R with the p norm function of the outer
    index of V. Then, we append Q to the scalar vector multiplication function
    of the the outer index of V and the quotient of 1 over the outer indexes
    of R. Return the result.

    Args:
        matrix_a: A matrix stored as a list of lists.

    Returns:
        A list producing the matrices Q and R.
    """
    Q: list = []
    V: list = [[0, 0], [0, 0]]
    R: list = [[0, 0], [0, 0]]
    for outer_index in range(len(matrix_a)):
        V[outer_index] = matrix_a[outer_index]
        for inner_index in range(0, outer_index):
            R[outer_index][inner_index] = LA.inner_product(Q[inner_index], V[outer_index])
            s = LA.scalar_vec_multi(Q[inner_index], -R[outer_index][inner_index])
            V[outer_index] = LA.add_vectors(V[outer_index], s)
        R[outer_index][outer_index] = LA.p_norm((V[outer_index]))
        Q.append(LA.scalar_vec_multi((V[outer_index]), (1/R[outer_index][outer_index])))
    return [Q, R]


#2
"""
matrix_a function which implements the stable version of Gram-Schmidt for reduced QR
factorization. It will take as it's argument a matrix and will return a list of 
two matrices. The first will be Q and the second will be R from the QR factorization 
described in the algorithm.
"""
def stable_gram_schmidt(matrix_a: list[list]) -> list[list]:
    """Computes QR factorization using the stable Gram-Schmidt process.

    Create an empty list for Q and V and a matrix of zeros for V and R.
    For each element in matrix a, append V. For each outer index, overwrite 
    the outer indexes of R with the p norm function of the outer index of V.
    This will be the same length of matrix a. Then, we append Q to the scalar 
    vector multiplication function of the the outer index of V and the quotient 
    of 1 over the outer indexes of R. For every inner index we have going from 
    the outer index to the length of matrix a, we will overwrite the inner
    and outer indexes of R with inner product function of the outer index of 
    Q and the inner index of V. Then, we will overwrite a variable, s, with
    the scalar vector multiplication function of outer index of Q, and the
    negative inner and outer indexes of R. Next, we will overwrite the inner 
    index of V with the add vectors function of the inner index of V and s.
    Return the result.

    Args:
        matrix_a: A matrix stored as a list of lists.

    Returns:
        A list producing the matrices Q and R.
    """
    Q: list = []
    V: list = []
    R: list = [[0, 0], [0, 0]]
    for element in matrix_a:
        V.append(element)
    for outer_index in range(len(matrix_a)):
        R[outer_index][outer_index] = LA.p_norm((V[outer_index]))
        Q.append(LA.scalar_vec_multi((V[outer_index]), (1 / R[outer_index][outer_index])))
        for inner_index in range(outer_index, len(matrix_a)):
            R[inner_index][outer_index] = LA.inner_product(Q[outer_index], V[inner_index])
            s = LA.scalar_vec_multi(Q[outer_index], -R[inner_index][outer_index])
            V[inner_index] = LA.add_vectors(V[inner_index], s)
    return [Q, R]