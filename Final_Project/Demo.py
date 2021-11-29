
import LA
import QR
import LS

print('Hello, my name is Sarah. This is the library I have written.')
print(' ')

print('''In this library, there are different files LA.py, QR.py, and LS.py that
demonstrate various linear algebraic operations. First, I will demonstrate the 
elementary linear algebraic operations in LA.py:''')
print(' ')

print('''The first function in LA.py is add_vectors. This function takes two vectors
as its arguments and returns their sum:''')
print('''For example, if vector_a = [1, 2, 3] and vector_b = [3, 6, 9], then add_vectors 
will return:''')
vector_a = [1, 2, 3]
vector_b = [3, 6, 9]
print(LA.add_vectors(vector_a, vector_b))
print(' ')

print('''The second function in LA.py is scalar_vec_multi. This function takes a vector
and and a scalar as its arguments and returns their product:''')
print('''For example, if vector_a = [1, 2, 3] and scalar_a = 2, then scalar_vec_multi
will return:''')
vector_a = [1, 2, 3]
scalar_a = 2
print(LA.scalar_vec_multi(vector_a, scalar_a))
print(' ')

print('''The third function in LA.py is scalar_mat_multi. This function takes a matrix
and and a scalar as its arguments and returns their product:''')
print('''For example, if matrix_a = [[1, 2], [2, 3]] and scalar_a = 2, then scalar_mat_multi
will return:''')
matrix_a = [[1, 2], [2, 3]]
scalar_a = 2
print(LA.scalar_mat_multi(matrix_a, scalar_a))
print(' ')

print('''The fourth function in LA.py is add_matrix. This function takes two matrices
as its arguments and returns their sum:''')
print('''For example, if matrix_a = [[1, 2], [2, 3]] and matrix_b = [[3, 1], [4, 2]], then add_matrix
will return:''')
matrix_a = [[1, 2], [2, 3]]
matrix_b = [[3, 1], [4, 2]]
print(LA.add_matrix(matrix_a, matrix_b))
print(' ')

print('''The fifth function in LA.py is mat_vec_multi. This function takes a matrix
and and a vector as its arguments and returns their product:''')
print('''For example, if matrix_a = [[1, 2], [2, 3]] and vector_c = [1, 2], then mat_vec_multi
will return:''')
matrix_a = [[1, 2], [2, 3]]
vector_c = [1, 2]
print(LA.mat_vec_multi(matrix_a, vector_c))
print(' ')

print('''The sixth function in LA.py is mat_multi. This function takes two matrices
as its arguments and returns their product:''')
print('''For example, if matrix_a = [[1, 2], [2, 3]] and matrix_b = [[3, 1], [4, 2]], then mat_multi
will return:''')
matrix_a = [[1, 2], [2, 3]]
matrix_b = [[3, 1], [4, 2]]
print(LA.mat_multi(matrix_a, matrix_b))
print(' ')

print('''The seventh function in LA.py is absolute_value. This function takes a scalar
as its argument and returns its absolute value:''')
print('''For example, if scalar_b = -3j+4, then absolute_value will return:''')
scalar_b = -3j+4
print(LA.absolute_value(scalar_b))
print(' ')

print('''The eighth function in LA.py is p_norm. This function takes a vector
as its argument and returns its p norm:''')
print('''For example, if vector_a = [1, 2, 3], then p_norm will return:''')
vector_a = [1, 2, 3]
print(LA.p_norm(vector_a))
print(' ')

print('''The ninth function in LA.py is infinity_norm. This function takes a vector
as its argument and returns its infinity norm:''')
print('''For example, if vector_a = [1, 2, 3], then infinity_norm will return:''')
vector_a = [1, 2, 3]
print(LA.infinity_norm(vector_a))
print(' ')

print('''The tenth function in LA.py is input_vector_norm. This function takes a vector
as its argument and returns its Computes the p-norm, which is the default, or the infinity norm:''')
print('''For example, if vector_d = [3, 2, 1], then input_vector_norm will return:''')
vector_d = [3, 2, 1]
print(LA.input_vector_norm(vector_d, 2, True))
print(' ')

print('''The eleventh function in LA.py is inner_product. This function takes two vectors
as its arguments and returns their inner product:''')
print('''For example, if vector_e = [1, 2, 3j] and vector_f = [2, 3j, 4], then inner_product 
will return:''')
vector_e = [1, 2, 3j]
vector_f = [2, 3j, 4]
print(LA.inner_product(vector_e, vector_f))
print(' ')

print('''Second, I will demonstrate different ways to compute QR factorizaton in QR.py:''')
print(' ')

print('''The first function in QR.py is stable_gram_schmidt. This function takes a matrix
as its argument and returns its QR factorization:''')
print('''For example, if matrix_01 = [[1, 0, 1], [2, 1, 0]], then stable_gram_schmidt will return:''')
matrix_01 = ([[1, 0, 1], [2, 1, 0]])
print(QR.stable_gram_schmidt(matrix_01))
print(' ')

print('''The second function in QR.py is orthonormalize. This function takes a matrix
as its argument and orthonormalizes it:''')
print('''For example, if matrix_01 = [[1, 0, 1], [2, 1, 0]], then orthonormalize will return:''')
matrix_01 = ([[1, 0, 1], [2, 1, 0]])
print(QR.orthonormalize(matrix_01))
print(' ')

print('''The third function in QR.py is conjugate. This function takes a scalar
as its argument and returns its conjugate:''')
print('''For example, if scalar_01 = 2 + 3j, then conjugate will return:''')
scalar_01 = 2 + 3j
print(QR.conjugate(scalar_01))
print(' ') 

print('''The fourth function in QR.py is conjugate_transpose. This function takes a matrix
as its argument and returns its conjugate transpose:''')
print('''For example, if matrix_02 = [[1, 0], [-5, -5]], then conjugate_transpose will return:''')
matrix_02 = [[1, 0], [-5, -5]]
print(QR.conjugate_transpose(matrix_02))
print(' ') 

print('''The fifth function in QR.py is deep_copy. This function takes a matrix
as its argument and returns its deep copy:''')
print('''For example, if matrix_02 = [[1, 0], [-5, -5]], then deep_copy will return:''')
matrix_02 = [[1, 0], [-5, -5]]
print(QR.deep_copy(matrix_02))
print(' ') 

print('''The sixth function in QR.py is sign. This function takes a scalar
as its argument and returns its sign:''')
print('''For example, if scalar_03 = -2, then sign will return:''')
scalar_03 = -2
print(QR.sign(scalar_03))
print(' ') 

print('''The seventh function in QR.py is V_builder. This function takes a vector
as its argument and returns its V_builder:''')
print('''For example, if vector_01 = [1, 0], then V_builder will return:''')
vector_01 = [1, 0]
print(QR.V_builder(vector_01))
print(' ') 

print('''The eighth function in QR.py is identity. This function takes a scalar
as its argument and returns its the square identity matrix:''')
print('''For example, if scalar_04 = 2, then identity will return:''')
scalar_04 = 2
print(QR.identity(scalar_04))
print(' ') 

print('''The ninth function in QR.py is vec_multi. This function takes two vectors
as its arguments and returns its their product:''')
print('''For example, if vector_01 = [1, 0] and vector_02 = [0, 3], then vec_multi will return:''')
vector_01 = [1, 0]
vector_02 = [0, 3]
print(QR.vec_multi(vector_01, vector_02))
print(' ') 

#START HERE
print('''The tenth function in QR.py is F_builder. This function takes a vector
as its argument and returns F:''')
print('''For example, if vector_01 = [1, 0], then F_Builder will return:''')
vector_01 = [1, 0]
print(QR.F_builder(vector_01))
print(' ') 

print('''The eleventh function in QR.py is Q_builder. This function takes a matrix
and a scalar as its arguments and returns Q:''')
print('''For example, if matrix_02 = [[1, 0], [-5, -5]] and scalar_03 = -2, 
then Q_builder will return:''')
matrix_02 = [[1, 0], [-5, -5]]
scalar_03 = -2
print(QR.Q_builder(matrix_02, scalar_03))
print(' ') 

print('''The twelfth function in QR.py is householder. This function takes a matrix
as its argument and returns its QR factorization:''')
print('''For example, if matrix_03 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]], then householder will return:''')
matrix_03 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
print(QR.householder(matrix_03))
print(' ') 

print('''Third, I will demonstrate how to compute the least squares matrix in LS.py:''')
print(' ')

print('''The first function in LS.py is backsub. This function takes a matrix
and a vector as its arguments and returns its backsub:''')
print('''For example, if matrix_01 = [[1, 2, 3], [1, 1, 2], [2, 1, 2]] and vector_01 = [3, 3, 1], 
then backsub will return:''')
matrix_01 = [[1, 2, 3], [1, 1, 2], [2, 1, 2]]
vector_01 = [3, 3, 1]
print(LS.backsub(matrix_01, vector_01))
print(' ')

print('''The second function in LS.py is least_squares. This function takes a matrix
and a vector as its arguments and returns its least squares matrix:''')
print('''For example, if matrix_01 = [[1, 2, 3], [1, 1, 2], [2, 1, 2]] and vector_01 = [3, 3, 1], 
then least_squares will return:''')
matrix_01 = [[1, 2, 3], [1, 1, 2], [2, 1, 2]]
vector_01 = [3, 3, 1]
print(LS.least_squares(matrix_01, vector_01))
print(' ')

print('''This concludes everything in my library. Thank you!''')
print(' ')