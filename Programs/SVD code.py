# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
# define a matrix
A = array([[2,3],[4,10]])
print(A)
# SVD
U, s, VT = svd(A)
print(U)
print(s)
print(VT)