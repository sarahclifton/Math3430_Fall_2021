#Uploaded Homework 5 on Wednesday Nov 3.
#Uploaded Homework 6 on Wednesday Nov 3.


"""
This assignment is due by 11:59pm on 11/05/2021. 

For this assignment you will be updating the python script QR.py from the
previous homework. As usual, all functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

1) Remove the function which implemented unstable Gram-Schmidt. It is unstable
and we may use the stable version exclusively from this point forward. 

2) Write a function which takes as it's argument a list of vectors and returns
an orthonormal list of vectors which shares the same span. 
"""

import LA

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


def orthonormalize(matrix_a: list[list]) -> list[list]:
    """Orthonormalizes a list of vectors.

    Short version of code:
    Retreives Q from the stable Gram Schmidt code.

    Long version of code:
    First, one must set the first column equal to u. This is 
    the vector we will use to find the the orthonormal vector one.
    To find the first orthonormal vector, find the quotient of 
    u over the magnitude of u. Repeat for all the columns of
    the matrix. Return the result.

    Args:
        matrix_a: A matrix stored as a list of lists.
    
    Returns:
        A orthonormalized list of vectors.
    """
    result: list[list] = stable_gram_schmidt(matrix_a)[0]
    return result
