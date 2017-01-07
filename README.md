# matrix_simulator
This is a Python program that simulates mathematical matrices. It is able to add, subtract, multiply (scalar and matrix),
and transpose matrices. In the future, I would like it to be able to swap rows/columns and be able to calculate the determinant of
square matrices

# Feature List:
The program currently has the following features
* Matrix addition/subtraction
* Matrix transposition
* Matrix multiplication (scalar and matrix)
* Viewing matrices

# Viewing Matrices:
The program is operated through the shell. To create a matrix you can instantiate a matrix object as follows:
  ```python
  matrix = Matrix(rows, columns, default_value)
  ```
The parameters are as follows:
* <b>rows</b>: the number of rows this matrix should have
* <b>columns</b>: the number of columns this matrix should have
* <b>default_value</b>: the default_value of the elements in this matrix (if no value is given, this value will be 0)

When getting a string representation of the matrix, the program will display it based on its rows
For example, a 3x3 matrix with the rows [1, 2, 3], [4, 5, 6], and [7, 8, 9] will be displayed as:
```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

# Matrix Addition/Subtraction:
You can add two matrices as follows where `sum_matrix` is the sum of the two matrices:
  ```python
  sum_matrix = matrix1.add(matrix2)
  ```
Similarly, you can subtract two matrices as follows where `difference_matrix` is the difference of the two matrices:
  ```python
  difference_matrix = matrix1.subtract(matrix2)
  ```
  
Given two matrices:
```python
[1, 2, 3]  [1, 2, 3]
[4, 5, 6]  [4, 5, 6]
[7, 8, 9]  [7, 8, 9]
```

Their sum will return the matrix:
```python
[2, 4, 6]
[8, 10, 12]
[14, 16, 18]
```

Their difference will return the matrix:
```python
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
```

The program requires that the two matrices be of the same dimensions (same number of rows and columns) otherwise it will raise a
`MatrixInvalidOperation` exception

# Matrix Transposition
Matrix transposition is the process described [here](https://en.wikipedia.org/wiki/Transpose).
Any matrix can be transposed. The dimensions do not matter for matrix transposition

A matrix can be transposed as follows where `transposed_matrix` is the transposed matrix:
  ```python
  transposed_matrix = matrix.transpose()
  ```
  
Given the following 2x3 matrix:
  ```python
  [1, 2, 3]
  [4, 5, 6]
  ```
  
The transposed matrix will result in:
  ```python
  [1, 4]
  [2, 5]
  [3, 6]
  ```
  
The property (A^T)^T (the transpose of a transpose) also holds. Transposing the transposed matrix will result in the original matrix

# Matrix multiplication
The program is capable of both matrix/matrix multiplication and scalar multiplication.
Scalar multiplication has no restrictions and can be done with any matrix

Scalar multiplication can be done as follows where `product_matrix` is the product matrix:
  ```python
  product_matrix = matrix.multiply_scalar(scalar)
  ```
The parameter `scalar` can be any scalar value

Given the following 3x3 matrix:
  ```python
  [1, 1, 1]
  [1, 1, 1]
  [1, 1, 1]
  ```

It multiplied by 3 will give the matrix:
  ```python
  [3, 3, 3]
  [3, 3, 3]
  [3, 3, 3]
  ```

Matrix multiplication is restricted to the dimensions of the two matrices.
You can only multiply two matrices together if the number of columns in the first matrix is equal to the number columns in the second.
Matrix multiplication is done as shown [here](https://en.wikipedia.org/wiki/Matrix_multiplication) using the dot product

Matrix multiplication can be done as follows where `product_matrix` is the product matrix:
  ```python
  product_matrix = matrix1.multiply(matrix2)
  ```
  
Given the following 3x3 matrices:
  ```python
  [3, 3, 3]  [3, 3, 3]
  [3, 3, 3]  [3, 3, 3]
  [3, 3, 3]  [3, 3, 3]
  ```
  
Their product will be the following 3x3 matrix:
  ```python
  [27, 27, 27]
  [27, 27, 27]
  [27, 27, 27]
  ```

Given an (n x m) matrix and an (m x p) matrix. The product matrix will always be an (n x p) matrix

# TODO list:
I would like to add the following features at some point to the program (in no particular order)

* ability to calculate determinants of square matrices
* ability to swap rows and columns

I would hope that one day I could implement features where the program can do more complicated matrix calculations (i.e. finding
eigenvalues, basis vectors, nullspace, etc) but those features are not of very high priority
