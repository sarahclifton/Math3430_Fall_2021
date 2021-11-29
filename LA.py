def add_vectors(vector_a: list, vector_b: list) -> list:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input. 
    Then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result


def scalar_vec_multi(vector: list, scalar: float) -> list:
    """Multplies the input scalar and the input vector.

    Creates a result vector, called result, as an empty list as a copy of 
    vector. Then multiplies the scalar by each the elements in the vector 
    and add it to the result. Return the desire result.

    Args:
        vector_a: A vector stored as a list.
        scalar_a: A scalar stored as a number.

    Returns:
        The product of the input scalar and the input vector stored as a list. 
    """
    result: list = []
    for index in range(len(vector)):
        result.append(vector[index] * scalar)
    return result


def scalar_mat_multi(matrix: list[list], scalar: float) -> list[list]:
    """Multiplies the input scalar and the input matrix.

    Creates a result matrix stored as a list of lists of 0's the same length as the input.
    Sets each element of the product of the matrix and scalar to the result, using the 
    scalar_vec_multi function. Replaces the 0's with the product of the inputs. 
    Repeat this for every corresponding element, and return the desire result.

    Args:
        matrix_a: A matrix stored as a list of lists. 
        scalar_a: A scalar stored as a number.

    Returns:
        The product of the input scalar and the input matrix. 
    """
    result: list[list[float]] = [0 for element in matrix]
    for index in range(len(result)):
        result[index] = scalar_vec_multi(matrix[index], scalar)
    return result


def add_matrix(matrix_a: list[list], matrix_b: list[list]) -> list[list]:
    """Adds the two input matrices.

    Creates a result matrix stored as a list of list of 0's the same length as the input.
    Then overwrites each element of the result vector with the corresponding element of 
    the sum of the input vectors. Sets each element of the sum of the matrices to the result, 
    using the add_vectors function. Replaces the 0 with the sum of the inputs, and repeat 
    this for every corresponding element. Return the desired result

    Args:
        matrix_a: A matrix stored as a list of lists.
        matrix_b: A matrix, the same length as matrix_a, stored as a list of lists.

    Returns:
        The sum of the two input matrices.
    """
    result: list = []
    for index in range(len(matrix_a)):
        x = add_vectors(matrix_a[index], matrix_b[index])
        result.append(x)
    return result


def mat_vec_multi(matrix: list[list], vector: list) -> list[list]:
    """Multiplies the input vector and the input matrix.

    Creates a result matrix stored as a list of list of 0's the same length as the input.
    Then, overwrites each element with its corresponding  product from the column vector
    which multiplies the corresponding column of the matrix. For each list in matrix, add
    the elements of the columns Replaces the 0 with the sum of the inputs, and return the 
    desired result.

    Args:
        matrix_a: A matrix stored as a list of lists.
        vector_c: A vector stored as a list.

    Returns:
        The product of the input vector and the input matrix. 
    """
    mat_result: list[list[float]] = [0 for elements in matrix]
    for index in range(len(vector)):
        mat_result[index] = scalar_vec_multi(matrix[index], vector[index])
    result = add_vectors(mat_result[0], mat_result[1])
    for index in range(2, len(mat_result)):
        result = add_vectors(result, mat_result[index])
    return result


def mat_multi(matrix_a: list[list], matrix_b: list[list]) -> list[list]:
    """Multiplies the two input matrices.

    Creates a result matrix, called result, as an empty list as a copy of matrix. 
    Sets each element of the product of the matrices to the result list of lists, 
    using the mat_vec_multi function. Replaces the 0's with the product of the inputs. 
    Repeat this for every corresponding element, and return the desire result.

    Args:
        matrix_a: A matrix stored as a list of lists.
        matrix_b: A matrix, the same length as matrix_a, stored as a list of lists.

    Returns:
        The product of the two input matrices. 
    """
    result: list[list[float]] = []
    for index in range(len(matrix_b)):
         result.append(mat_vec_multi(matrix_a, matrix_b[index]))
    return result


def absolute_value(scalar: complex or float) -> complex or float:
    """Takes the input scalar and computes the absolute value of it.

    We take the absolute value of a scalar. It then becomes positive no matter
    if it is a complex, negative, or positive value.

    Args:
        scalar: A scalar stored as a float or complex number.
        
    Returns:
        The positive absolute value of a scalar stored as a complex or a float number.
    """
    result: complex or float = ((scalar.real**2 + scalar.imag**2)**(1/2))
    return result


def p_norm(vector: list, p: int = 2) -> float:
    """This function computes the p-norm of the input vector. The p-norm is 
    defaulted to 2.

    We first take a float that represents the result and sets it equal to zero. 
    Then we find that if the element in the vector is greater than 0, we add the 
    element to the power of the absolute value of p to the result. If the element
    in the vector is anything else, we add the negative element to the power of 
    the absolute value of p to the result. Finally, we take the absolute value 
    of the pth power of the result and add it to the result.

    Args:
        vector: A vector stored as a list.
        p: A positive integer defaulted to 2.
        
    Returns:
        The p-norm of the input vector stored as a float.
        
    """
    result: float = 0
    for index in vector:
        if index > 0:
            result += index**(abs(p))
        else:
            result += (-index)**(abs(p))
    result = result**(abs(1/p))
    return result


def infinity_norm(vector: list) -> float:
    """This function computes the infinity norm of the input vector.

    First we set the result to an empty vector and we overwrite every
    element in the vector with the absolute value of each element and
    add it to the result. We then return the highest value of the result 
    stored as a float.

    Args:
        vector: a vector stored as a list.

    Returns:
        The infinity norm of the input vector stored as a float.
        
    """
    result: list[float] = []
    for element in range(len(vector)):
        result.append(abs(vector[element]))
    return float(max(result))


def input_vector_norm(vector: list, p: float = 2, boolean: bool = False) -> float:
    """Computes the p-norm, which is the default, or the infinity norm.

    If the boolean is true, then we comput the infinity norm and return the result.
    For anything else, it is false, and we compute the p norm. Then we return the result.

    Args:
        vector: A vector stored as a list.
        scalar: A float valued scalar, set to default as 2.
        A boolean value, set to the default as False.

    Returns:
        the p-norm, which is the default, or the infinity norm stored as a float.
        
    """

    if (boolean == False): 
        return float(p_norm(vector, p))
    else: 
        return float(infinity_norm(vector))


def inner_product(vector_a: list[complex or float], vector_b: list[complex or float]) -> complex or float:
    """Computes the inner product of the two input vectors.
    
    First set the result to an empty float or complex number. Then we overwrite every index in result with
    the product of each element in the vector_a and every element in vector_b. We then add all the products
    together and return our desired result.

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector the same length as vector_a, stored as a list.

    Returns:
        The inner product of the two input vectors stored as a complex or a float number.
        
    """

    result: float or complex = 0 + 0j or 0
    for index in range(len(vector_a)):
        result += vector_a[index]*vector_b[index]
    return result