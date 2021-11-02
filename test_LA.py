
import LA
import pytest

#Test 1
vector_a = [1, 2, 3]
vector_b = [3, 6, 9]
vector_c = [1, 2]
scalar_a = 2
matrix_a = [[1, 2], [2, 3]]
matrix_b = [[3, 1], [4, 2]]

#Test 2
vector_d = [2, 3, 4]
vector_e = [4, 5, 6]
vector_f = [2, 3]
scalar_b = 3
matrix_c = [[3, 2], [3, 2]]
matrix_d = [[1, 3], [2, 3]]


#0
def test_add_vectors():
    #vector_a = LA.vector_a
    #vector_b = LA.vector_b
    #[1+3, 2+6, 3+9] = [4, 8, 12]
    assert LA.add_vectors(vector_a, vector_b) == [4, 8, 12]
    #vector_d = LA.vector_d
    #vector_e = LA.vector_e
    #[2+4, 3+5, 4+6] = [6, 8, 10]
    assert LA.add_vectors(vector_d, vector_e) == [6, 8, 10]

#1
def test_scalar_vec_multi():
    #vector_a = LA.vector_a
    #scalar_a = LA.scalar_a
    #[2(1). 2(2), 2(3)] = [2, 4, 6]
    assert LA.scalar_vec_multi(vector_a, scalar_a) == [2, 4, 6]
    #vector_d = LA.vector_d
    #scalar_b = LA.scalar_b
    #[3(2), 3(3), 3(4)] = [6, 9, 12]
    assert LA.scalar_vec_multi(vector_d, scalar_b) == [6, 9, 12]

#2
def test_scalar_mat_multi():
    #matrix_a = LA.matrix_a
    #scalar_a = LA.scalar_a
    #[[2(1). 2(2)], [2(2). 2(3)]] = [[2, 4], [4, 6]]
    assert LA.scalar_mat_multi(matrix_a, scalar_a) == [[2, 4], [4, 6]]
    #matrix_c = LA.matrix_c
    #scalar_b = LA.scalar_b
    #[[3(3), 3(2)], [3(3), 3(2)]] = [[9, 6], [9, 6]]
    assert LA.scalar_mat_multi(matrix_c, scalar_b) == [[9, 6], [9, 6]]

#3 
def test_add_matrix():
    #matrix_a = LA.matrix_a
    #matrix_b = LA.matrix_b
    #[[1+3. 2+1],[2+4, 3+2]] = [[4, 3], [6, 5]]
    assert LA.add_matrix(matrix_a, matrix_b) == [[4, 3], [6, 5]]
    #matrix_c = LA.matrix_c
    #matrix_d = LA.matrix_d
    #[[3+1, 3+1], [2+3, 2+3]] = [[4, 5], [5, 5]]
    assert LA.add_matrix(matrix_c, matrix_d) == [[4, 5], [5, 5]]

#4
def test_mat_vec_multi():
    #matrix_a = LA.matrix_a
    #vector_c = LA.vector_c
    #[(1(1) + 2(2)), 1(2) + 3(2)] = [5, 8]
    assert LA.mat_vec_multi(matrix_a, vector_c) == [5, 8]
    #matrix_c = LA.matrix_c
    #vector_f = LA.vector_f
    #[(3(2) + 3(3)), 2(2) + 2(3)] = [15, 10]
    assert LA.mat_vec_multi(matrix_c, vector_f) == [15, 10]

#5
def test_mat_multi():
    #matrix_a = LA.matrix_a
    #matrix_b = LA.matrix_b
    #[[1(3) + 2(1), 2(3) + 3(1)], [1(4) + 2(2), 2(4) + 3(2)]] = [[5, 9], [8, 14]]
    assert LA.mat_multi(matrix_a, matrix_b) == [[5, 9], [8, 14]]
    #matrix_c = LA.matrix_c
    #matrix_d = LA.matrix_d
    #[[3(1) + 3(3), 2(1) + 2(3)], [3(2) + 3(3), 2(2) + 2(3)]] = [[12, 8], [15, 10]]
    assert LA.mat_multi(matrix_c, matrix_d) == [[12, 8], [15, 10]]


#HW 4

#1
test_scalar_01 = -3j+4
test_scalar_02 = -2
def test_absolute_value():
    assert LA.absolute_value(test_scalar_01) == 5
    assert LA.absolute_value(test_scalar_02) == 2

#2
test_vector_01 = [1, 2, 3]
test_vector_02 = [2, 3, 4]
def test_p_norm():
    assert LA.p_norm(test_vector_01) == 3.7416573867739413
    assert LA.p_norm(test_vector_02) == 5.385164807134504

#3
test_vector_01 = [1, 2, 3]
test_vector_02 = [2, 3, 4]
def test_infinity_norm():
    assert LA.infinity_norm(test_vector_01) == 3
    assert LA.infinity_norm(test_vector_02) == 4

#4
test_vector_03 = [3, 2, 1]
test_vector_04 = [1, -2, 3]
def test_input_vector_norm():
    assert LA.input_vector_norm(test_vector_03, 2, True) == 3
    assert LA.input_vector_norm(test_vector_04, 2, True) == 3

#5
test_vector_05 = [1, 2, 3j]
test_vector_06 = [2, 3j, 4]
test_vector_07 = [3, 2, 1]
test_vector_08 = [-3, 4, 1]
def test_inner_product():
    #dot product = 1(2) + 2(3j) + 3j(4) = 2 + 18j
    assert LA.inner_product(test_vector_05, test_vector_06) == 2 + (18j)
    #dot product = 3(-3) + 2(4) + 1(1) = 0
    assert LA.inner_product(test_vector_07, test_vector_08) == 0