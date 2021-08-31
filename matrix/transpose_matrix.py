"""
transpose a matrix
[1, 2]
[3, 4]
[5, 6]


[1, 3, 5]
[2, 4, 6]
"""
def transpose_matrix(m):
	N, M = len(m[0]), len(m)
	orig = [[m[i][j] for j in range(N)] for i in range(M)]
	print(orig)
	transposed = [[m[j][i] for j in range(M)] for i in range(N)]
	return transposed



def transpose_matrix_alt1(m):

	matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
	print([i for i in matrix])
	t_matrix=map(list, zip(*matrix))
	return [i for i in t_matrix]


def rotate_image_inplace(A):
    A.reverse()
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]

m = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print(transpose_matrix_alt1(m))
#print(transpose_matrix(m))