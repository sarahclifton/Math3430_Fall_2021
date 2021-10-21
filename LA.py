"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 
"""

#0
"""
A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.
"""

def add_vectors(vector_a: list[float], vector_b: list[float]) -> list[float]:
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

# End Example
# Note that you must add unit tests for problem 0!!!!!

#1
"""
A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.
"""

def scalar_vec_multi(vector: list[float], scalar: float) -> list[float]:
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
    result: list[float] = []
    for index in range(len(vector)):
        result.append(vector[index] * scalar)
    return result

#2
"""
A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.
"""

def scalar_mat_multi(matrix: list[list[float]], scalar: float) -> list[list[float]]:
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

#3
"""
A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.
"""

def add_matrix(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
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
    result: list[list[float]] = [0 for element in matrix_a]
    for index in range(len(result)):
        result[index] = add_vectors(matrix_a[index], matrix_b[index])
    return result

#4
"""
A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.
"""

def mat_vec_multi(matrix: list[float], vector:list[float]) -> list[list[float]]:
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

#5
"""
A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""

def mat_multi(matrix_a: list[float], matrix_b: list[float]) -> list[list[float]]:
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

#HW_04

"""
This assignment is due by 11:59pm on 10/22/2021. 

For this assignment you will be adding functinons to the LA.py script from HW03.
All functions must satisfy the same requirements as in HW03. The functions you
will need to add are
"""

#1
"""
A function which takes a scalar as it's input and returns it's absolute
value. Note that this function must be able to take both real numbers and
complex numbers as input!!!
"""

def absolute_value(scalar: complex or float) -> complex or float:
    """Takes the input scalar and computes the absolute value of it.

    We take the absolute value of a scalar. It then becomes positive no matter
    if it is a complex, negative, or positive value.

    Args:
        scalar: A scalar stored as a float or complex number.
        
    Returns:
        The positive absolute value of a scalar stored as a complex or a float number.
    """
    result: complex or float = abs(scalar)
    return result

#test:
test_scalar_01 = -3
test_scalar_02 = 2

print(absolute_value(test_scalar_01))
print(absolute_value(test_scalar_02))


#2
"""
A function which takes the as it's arguments

1) A vector stored as a list.

2) A float valued scalar, set to default as 2. 

and returns the p-norm of the input vector. Which p-norm must be determined using
the float valued scalar input. If no argument is given, it should default to
2.
"""

def p_norm(vector:list[float], p: int = 2) -> float:
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

#test:
test_vector_01 = [1, 2, 3]
test_vector_02 = [2, 3, 4]

print(p_norm(test_vector_01))
print(p_norm(test_vector_02))

#3
"""
A function which takes as it's argument a vector stored as a list and
returns the infinity norm of the input vector.
"""

def infinity_norm(vector: list[float]) -> float:
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

#test:
test_vector_01 = [1, 2, 3]
test_vector_02 = [2, 3, 4]

print(infinity_norm(test_vector_01))
print(infinity_norm(test_vector_02))

#4
"""
A function which takes as it's arguments

1) A vector stored as a list.

2) An float valued scalar, set to default as 2.

3) A boolean value, set to default as False.

The function will return the p-norm of the input vector. If the boolean value is
given as True, the function will return the infinity norm of the input vector.
Otherwise it will return the p-norm of the vector corresponding to the float 
scalar argument. This function must use the functions from problem #2 and
problem #3 to earn credit. 
"""

def input_vector_norm(vector: list[float], p: float = 2, boolean: bool = False) -> float:
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

#test
test_vector_03 = [3, 2, 1]
test_vector_04 = [1, -2, 3]

print(input_vector_norm(test_vector_03, 2, True))
print(input_vector_norm(test_vector_04, 2, True))


#5
"""
A function which takes as it's arguments two vectors, stored as lists. This
function then returns the inner product of these vectors. Your function must be
able to handle complex numbers!
"""

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

#test
test_vector_05 = [1, 2, 3j]
test_vector_06 = [2, 3j, 4]
# dot product = 1(2) + 2(3j) + 3j(4) = 2 + 8j
test_vector_07 = [3, 2, 1]
test_vector_08 = [-3, 4, 1]
# dot product = 3(-3) + 2(4) + 1(1) = 0

print(inner_product(test_vector_05, test_vector_06))
print(inner_product(test_vector_07, test_vector_08))
