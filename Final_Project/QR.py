import LA


#HW 05

def unstable_gram_schmidt(matrix_a: list[list]) -> list[list]: 
    """Computes QR factorization using the unstable Gram-Schmidt process. 

    Create an index list for Q and a matrix of zeros for V and R. For each
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


def stable_gram_schmidt(matrix_a: list[list]) -> list[list]:
    """Computes QR factorization using the stable Gram-Schmidt process.

    Create an index list for Q and V and a matrix of zeros for V and R.
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


#HW 06

def orthonormalize(matrix_a: list[list]) -> list[list]:
    """Orthonormalizes a list of vectors.

    Short version of code:
    Retreives Q from the stable Gram Schmidt code.

    Long version of code:
    First, one must set the first outer_index equal to u. This is 
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


#HW 07

def conjugate(scalar: float) -> float:
    """Calculates the conjugate of the input scalar

    First we set the result equal to the real scalar
    plus the negative imaginary scalar multiplied 
    by 1j. Return the desired result

    Args:
        scalar: A scalar stored as a float

    Returns:
        The conjugated scalar
    """
    result = scalar.real + -scalar.imag*1j
    return result


def conjugate_transpose(matrix_a):
    """Calculates the conjugate transpose of the input matrix.

    First, we create two matrices in which we fill with zeros.
    Then we replace those zeros with the conjugated matrix. With
    the other matrix, wechange the rows and columns. Return the
    desired result.

    Args:
        matrix_a: A matrix stored as a list of lists.

    Returns:
        The conjugated transpose of the input matrix.
    """
    result: list = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    temp: list = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    for x in range(len(matrix_a[0])):
        for y in range(len(matrix_a[0])):
            result[x][y] = matrix_a[x][y].conjugate()
    for index in range(len(matrix_a[0])):
        for element in range(len(matrix_a)):
            temp[index][element] = result[element][index]
    return temp


def deep_copy(matrix_a: list[list]) -> list[list]:
    """Creates a deep copy of the input matrix.

    First we set a matrix equal to all the zeros. Then
    we replace all the elements with the other matrix
    we are trying to copy. Return the desired result.

    Args:
        matrix_a: A matrix stored as a list of lists.

    Returns:
        A deep copy of the input matrix.
    """
    index = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    for x in range(len(matrix_a[0])):
        for y in range(len(matrix_a[0])):
            index[x][y] = matrix_a[x][y]
    return index


def sign(a: float) -> float:
    """Creates the sign

    First, check if the number is greater than zero.
    Then, if the number is less than zero, return -1.
    If the number is greater than zero, return 1.

    Args:
        a: A number stored as a float

    Returns:
        -1 or 1.
    """
    if a < 0:
        return -1
    else:
        return 1


def V_builder(vector_a: list) -> list:
    """Calculates the reflection of the input vector

    First we create a vector a, which we put the first
    index of a equal to 1. Then, we find the scalar vector
    multiplication of the multiplication of the sign of the 
    first index of vector_a and the p_norm of vector and a.
    We then use add_vectors to add this to vector_a. Return V.

    Args:
        vector_a: A vector stored as a list.

    Returns:
        The reflection of the input vector.
    """
    a = [0 for element in range(len(vector_a))]
    a[0] = 1
    V = LA.add_vectors(vector_a, LA.scalar_vec_multi(a, sign(vector_a[0])*LA.p_norm(vector_a)))
    return V


def identity(matrix_a: int) -> int:
    """Finds the identity matrix.

    First we create a matrix that for every element in the matrix
    is equal to zero. Then for all of the diagonal elements, replace
    them with 1.

    Args:
        matrix_a: A matrix stored as a list of lists.

    Returns:
        The identity matrix.
    """
    identity = [[0 for element in range(matrix_a)] for index in range(matrix_a)]
    for x in range(matrix_a):
        identity[x][x] = 1
    return identity


def vec_multi(vector_a, vector_b):
    """Calculates the product of two vectors

    First we set our result equal to an index set.
    Then for every index in the range of length
    of vector_a, we append the scalar_vec_multi of 
    vector_a and vector_b to the result. Return the
    desired result.

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector stored as a list.

    Returns:
        The product of two vectors.
    """
    result: list = []
    for x in range(len(vector_a)):
        result.append(LA.scalar_vec_multi(vector_b, vector_a[x]))
    return result    


def F_builder(vector_a: list) -> list:
    """Calculates the F_k value

    First we set a scalar, s, equal to the fraction of
    -2 over the p_norm of vector_a squared. Then, we use
    the scalar_vec_multi of the scalar, s, and the multiplication
    of vector_a and vector_a and set it equal to x. We 
    then use the add_matrix of the identity matrix and x.
    Return the desired result.

    Args:
        vector_a: A vector stored as a list.

    Returns:
        The F_k value
    """
    s = -2/(LA.p_norm(vector_a))**2
    x = LA.scalar_mat_multi(vec_multi(vector_a, vector_a), s)
    y = LA.add_matrix(identity(len(vector_a)), x)
    return y


def Q_builder(matrix_a: list[list], k: int) -> list:
    """Creates the Q_builder function

    First, we set the elements of the input matrix to zero.
    Then for every index with the length of matrix_a, and for
    every element in the range with the length of the index of
    matrix_a, if the scalar plus the index or the scalar plus 
    the element is less than the length of the index of matrix_a,
    then overwrite the index and element of Q is with the scalar
    plus index and the scalar plus element of matix_a. Set v equal
    to the V_builder of the first element of Q. Set f equal to the
    F_builder of v. Then, set Q_builder equal to the identity with
    the length of matrix_a. For the inde in the range of the scalar
    to the length of Q_builder, overwrite the index and element of
    Q_builder with the index minus the scalr and the element minus
    the scalar of f. Return the desired result.

    Args:
        matrix_a: A matrix stored as a list of lists.

    Returns:
        The Q_builder function
    """
    Q: list = [[0 for element in range(k, len(matrix_a[index]))] for index in range(k, len(matrix_a))]
    for index in range(len(matrix_a)):
        for element in range(len(matrix_a[index])):
            if k+index < len(matrix_a[index]):
                if k+element < len(matrix_a[index]):
                    Q[index][element] = matrix_a[k+index][k+element]
    v = V_builder(Q[0])
    f = F_builder(v)
    Q_builder = identity(len(matrix_a))
    for index in range(k, len(Q_builder)):
        for element in range(k, len(Q_builder)):
            Q_builder[index][element] = f[index-k][element-k]
    return Q_builder


def householder(matrix_a: list[list]) -> list:
    """Creates the householder function

    First set R equal to the deep_copy of matrix_a.
    Then, set Q_list to an empty set. For every element
    in range of the length of R, set Q_temp equal to the
    Q_builder of R and k, set R equal to the mat_multi of
    Q_temp and R, and append Q_list to Q_temp. Set Q equal
    to the negatove Q_list and the conjugate_transpose of
    the first element of Q_list. For the index in the range
    of 1 to the length of Q_list, set Q equal to the mat_multi
    of Q anf the conjugate_transpose of the index of Q_list.
    Return the desired result.

    Args:
        matrix_a: a matrix stored as a list of lists.
    
    Returns:
        The housholder function
    """
    R: list = deep_copy(matrix_a)
    Q_list: list = []
    for k in range(len(R)):
        Q_temp: list = Q_builder(R, k)
        R = LA.mat_multi(Q_temp, R)
        Q_list.append(Q_temp)
    Q: list = Q_list[-1]
    Q: list = conjugate_transpose(Q_list[0])
    for index in range(1, len(Q_list)):
        Q = LA.mat_multi(Q, conjugate_transpose(Q_list[index]))
    return [Q, R]