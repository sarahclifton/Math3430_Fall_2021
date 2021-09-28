#Problem 01


#Plan
"""
-The Three Questions
Q1: What do we have?

A1: A vector stored as a list and a scalar. Denoted by the names vector and scalar.

Q2: What do we want?

A2: The product between the scalar and the vector stored as a list.

Q3: How will we get there?

A3: Create a result vector, called result, and multiply the scalar by each corresponding element of the vector and store it as a list.

-Pseudocode

Step 00: Call this algorithm scalar_vec_multi(scalar, vector).

Step 01: Set up the result to be a copy of vector.

Step 02: Multiply the scalar by each the elements in the vector.

Step 03: Return the desire result.
"""


#Implement
def scalar_vec_multi(scalar, vector):
    result = [0 for element in vector]
    for index in range(len(result)):
        result[index] = scalar * vector[index]
    return result


#Test Inputs
test_vector_01 = [1, 2, 3]
test_scalar_01 = 2

print('Test Output for scalar_vec_multi:' + str(scalar_vec_multi(test_scalar_01, test_vector_01)))
print('Should have been [2, 4, 6]')

test_vector_02 = [3, 1, 2]
test_scalar_02 = 2

print('Test Output for scalar_vec_multi:' + str(scalar_vec_multi(test_scalar_02, test_vector_02)))
print('Should have been [6, 2, 4]')



#Problem 02


#Plan
"""
-The Three Questions
Q1: What do we have?

A1: A matrix stored as a list of lists and a scalar. The matrix is denoted as matrix and the scalar as scalar. Each list in matrix represents a column vector.

Q2: What do we want?

A2: The product between the scalar and the matrix stored as a list.

Q3: How will we get there?

A3: Multiply the scalar by each corresponding element of the matrix and store it as a list.

-Pseudocode

Step 00: Call this algorithm scalar_mat_multi(scalar, matrix).

Step 01: Set up an empty list for the result.

Step 02: Add elements of the same number of the range of the vector to the "result" and set it equal to 0.

Step 03: In a matrix, we will have the rows equal to a empty list.

Step 04: Set each element of the product of the matrix and vector to the result list. Replace the 0 with the product of the inputs. Repeat this for every corresponding element.

Step 05: Return the desire result.
"""


#Implement
def scalar_mat_multi(scalar, matrix):
    result = []
    row = []
    for rows in matrix:
        row = [0 for element in rows]
        result.append (row)
    for index in range(len(result)):
        for row_index in range(len(result[index])):
            result[index][row_index] = scalar*matrix[index][row_index]
    return result


#Test Inputs
test_matrix_01 = [[1, 2, 3], [2, 3, 1]]
test_scalar_01 = 2

print('Test Output for scalar_mat_multi:' + str(scalar_mat_multi(test_scalar_01, test_matrix_01)))
print('Should have been [[2, 4, 6], [4, 6, 2]]')

test_matrix_02 = [[2, 3, 3], [2, 2, 1]]
test_scalar_02 = 2

print('Test Output for scalar_mat_multi:' + str(scalar_mat_multi(test_scalar_02, test_matrix_02)))
print('Should have been [[4, 6, 6], [4, 4, 2]]')



#Problem 03


#Plan
"""
-The Three Questions
Q1: What do we have?

A1: Two matrices with the same dimensions stored as lists of columns. These matrices are denoted as matrix_a and matrix_b.

Q2: What do we want?

A2: The sum of matrix_a and matrix_b stored as a list.

Q3: How will we get there?

A3: We will have a result matrix as a copy of matrix_a. Add each elements of the column of matrix_a to the corresponding elements of column of matrix_b to create a new matrix and store it as a list.

-Pseudocode

Step 00: Call this algorithm add_matrix(matrix_a, matrix_b).

Step 01: Set up an empty list for the result.

Step 02: Add elements of the same number of the range of the vector to the "result" and set it equal to 0.

Step 03: In a matrix, we will have the rows equal to a empty list.

Step 04: Set each element of the sum of the matrices to the result list. Replace the 0 with the sum of the inputs. Repeat this for every corresponding element.

Step 05: Return the desire result.
"""


#Implement
def add_matrix(matrix_a, matrix_b):
    result = []
    row = []
    for rows in matrix_a:
        row = [0 for element in rows]
        result.append (row)
    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[0])):    
            result[row][column] = matrix_a[row][column] + matrix_b[row][column]
    return result


#Test Inputs
test_matrix_a = [[1, 2, 3], [2, 3, 1]]
test_matrix_b = [[3, 2, 1], [1, 2, 3]]

print('Test Output for add_matrix:' + str(add_matrix(test_matrix_a, test_matrix_b)))
print('Should have been [[4, 4, 4], [3, 5, 4]]')

test_matrix_c = [[1, 1, 1], [2, 2, 2]]
test_matrix_d = [[3, 3, 3], [1, 2, 3]]

print('Test Output for add_matrix:' + str(add_matrix(test_matrix_c, test_matrix_d)))
print('Should have been [[4, 4, 4], [3, 4, 5]]')



#Problem 04


#Plan
"""
-The Three Questions
Q1: What do we have?

A1: A matrix and vector stored as lists of columns. Each component list represents a column of the matrix The matrix is denoted as matrix and the vector is as vector.

Q2: What do we want?

A2: The product of the matrix and the vector stored as a list.

Q3: How will we get there?

A3: Set each element of the product of the matrix and vector to the result list. Replace the 0 with the product of the inputs. Multiply the elements of the matrix to the corresponding elements of the vector and store it as a list.

-Pseudocode

Step 00: Call this algorithm mat_vec(matrix, vector).

Step 01: Set up an empty list for the result.

Step 02: Add elements of the same number of the range of the vector to the "result" and set it equal to 0.

Step 03: For each list in matrix, override it as the result from scalar_vec_multi(corresponding element of vector, list).

Step 04: For each list in matrix, set result = result + list

Step 05: Return the desire result.
"""


#Implement
def scalar_vec_multi(scalar, vector):
    result = [0 for element in vector]
    for index in range(len(result)):
        result[index] = scalar * vector[index]
    return result

def mat_vec_multi(matrix, vector):
    result = []
    for index in vector:
        result.append (0)
    for index in range(len(vector)):
                   for index in range(len(scalar_vec_multi(vector[index], matrix[index]))):
                                      result[index] *= scalar_vec_multi(vector[index], matrix[index])[index]
    return result


#Test Inputs
test_matrix_01 = [[1, 2], [2, 3]]
test_vector_01 = [3, 1]

print('Test Output for add_matrix:' + str(mat_vec_multi(test_matrix_01, test_vector_01)))
print('Should have been [5, 9]')

test_matrix_02 = [[3, 1], [1, 2]]
test_vector_02 = [3, 1]

print('Test Output for add_matrix:' + str(mat_vec_multi(test_matrix_02, test_vector_02)))
print('Should have been [10, 5]')



#Problem 05


#Plan
"""
-The Three Questions
Q1: What do we have?

A1: Two matrices stored as lists of lists. The amount of columns of matrix_a should match the amount of rows of matrix_b. Both matrices are denoted as a list of vectors.

Q2: What do we want?

A2: The product of the matrices stored as a list.

Q3: How will we get there?

A3: We will create a result matrix which is a copy of matrix_b, called result. Then for each element of result, we will override it with the output of mat_vec(matrix_a, component).

-Pseudocode

Step 00: Call this algorithm mult_matrices(matrix_a, matrix_b).

Step 01: Set up an empty list for the result.

Step 02: Add elements of the same number of the range of the vector to the "result" and set it equal to 0.

Step 03: Initialize result as a copy of matrix_b and for column in result, set column = mat_vec(matrix_a, column)

Step 04: Return the desire result.
"""


#Implement
def scalar_vec_multi(scalar, vector):
    result = [0 for element in vector]
    for index in range(len(result)):
        result[index] = scalar * vector[index]
    return result

def mat_vec_multi(matrix, vector):
    result = []
    for index in vector:
        result.append (0)
    for index in range(len(vector)):
                   for index in range(len(scalar_vec_multi(vector[index], matrix[index]))):
                                      result[index] *= scalar_vec_multi(vector[index], matrix[index])[index]
    return result

def mat_multi(matrix_a, matrix_b):
    result = []
    for index in matrix_b:
         result.append (mat_vec_multi(matrix_a, matrix_b))
    return result


#Test Inputs
test_matrix_01 = [[1, 2], [2, 3]]
test_matrix_02 = [[3, 1], [4, 2]]

print('Test Output for mat_multi:' + str(mat_multi(test_matrix_01, test_matrix_02)))
print('Should have been [[5, 8], [9, 14]]')

test_matrix_03 = [[5, 3], [1, 2]]
test_matrix_04 = [[1, 3], [3, 4]]

print('Test Output for mat_multi:' + str(mat_multi(test_matrix_01, test_matrix_02)))
print('Should have been [[8, 8], [19, 17]]')

