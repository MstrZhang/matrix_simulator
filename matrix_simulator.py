#### EXCEPTIONS ####

class MatrixIndexError(Exception):
    ''' An attempt has been made to access an invalid index in this matrix '''
    pass

class MatrixInvalidOperation(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''
    pass

#### HELPER FUNCTIONS ####

def dot_product(first_list, second_list):
    ''' (list of float, list of float) -> float
    Given two lists of floats, determines the dot product
    The dot product is the sum of the product of each component of two vectors
    REQ: the length of both lists must be the same
    '''
    result = 0
    for i in range(0, len(first_list)):
        result += first_list[i] * second_list[i]

    return result

#### MATRIX ####

class Matrix():
    ''' A class to represent a mathematical matrix '''

    def __init__(self, m, n, default=0):
        ''' (Matrix, int, int, float) -> NoneType
        Creates a new (m x n) matrix with the given default value (0 if no value is given)
        '''
        self._rows = m
        self._cols = n
        self._matrix = []

        for i in range(0, self._rows):
            self._matrix.append([default] * (self._cols))

    def __str__(self):
        ''' (Matrix) -> str
        Returns a string representation of this Matrix
        '''
        result = ""

        for row in self._matrix:
            result += str(row) + "\n"

        return result

    def add(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Adds two matrices together based on the mathematical definition of matrix addition
        REQ: both matrices must be the same size (same length rows and columns)
        '''
        if ((self._rows != other.get_rows()) or (self._cols != other.get_cols())):
            raise MatrixInvalidOperation("cannot add two matrices of different sizes")

        new_matrix = Matrix(self._rows, self._cols)
        for i in range(0, self._rows):
            for j in range(0, self._cols):
                new_matrix.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))

        return new_matrix

    def subtract(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Subtracts two matrices together based on the mathematical definition of matrix subtraction
        REQ: both matrices must be the same size (same length rows and columns)
        '''
        if ((self._rows != other.get_rows()) or (self._cols != other.get_cols())):
            raise MatrixInvalidOperation("cannot subtract two matrices of different sizes")

        new_matrix = Matrix(self._rows, self._cols)
        for i in range(0, self._rows):
            for j in range(0, self._cols):
                new_matrix.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))

        return new_matrix

    def transpose(self):
        ''' (Matrix) -> Matrix
        Transposes the matrix based on the mathematical definition of matrix transposition
        (changes the rows to columns and the columns to rows; rotates the matrix by 45 degrees)
        '''
        new_rows = []
        for i in range(0, self._cols):
            new_rows.append(self.get_col(i))

        matrix = Matrix(self._cols, self._rows)
        for i in range(0, matrix.get_rows()):
            matrix.set_row(i, new_rows[i])

        return matrix

    def multiply_scalar(self, scalar):
        ''' (Matrix, float) -> Matrix
        Multiplies the matrix by a scalar value based on the mathematical definition of scalar multiplication
        '''
        matrix = Matrix(self._cols, self._rows)
        for i in range(0, self._rows):
            for j in range(0, self._cols):
                matrix.set_element(i, j, self.get_element(i, j) * scalar)

        return matrix

    def multiply(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Multiplies two matrices together based on the mathematical definition of matrix multiplication
        REQ: the number of columns of the first matrix must be equal to the number of rows of the second matrix
        '''
        if (self._cols != other.get_rows()):
            raise MatrixInvalidOperation("cannot multiply matrices of these dimensions")

        matrix = Matrix(self._rows, other.get_cols())
        for i in range(0, matrix.get_rows()):
            for j in range(0, matrix.get_cols()):

                matrix.set_element(i, j, dot_product(self.get_row(i), other.get_col(j)))

        return matrix

    def get_element(self, row, col):
        ''' (Matrix, int, int) -> float
        Returns the element at the given index
        '''
        return self._matrix[row][col]

    def get_rows(self):
        ''' (Matrix) -> int
        Returns the number of rows in this Matrix
        '''
        return self._rows

    def get_cols(self):
        ''' (Matrix) -> int
        Returns the number of columns in this Matrix
        '''
        return self._cols

    def get_row(self, index):
        ''' (Matrix, int) -> list of float
        Returns the entire row given the index
        '''
        if ((index > self._rows) or (index < 0)):
            raise MatrixIndexError("the given index is out of bounds")

        return self._matrix[index]

    def get_col(self, index):
        ''' (Matrix, int) -> list of float
        Returns the entire column given the index
        '''
        if ((index > self._cols) or (index < 0)):
            raise MatrixIndexError("the given index is out of bounds")

        cols = []
        for row in self._matrix:
            cols.append(row[index])

        return cols

    def set_element(self, row, col, new_element):
        ''' (Matrix, int, int, float) -> NoneType
        Sets the given index to the value of new_element
        '''
        self._matrix[row][col] = new_element

    def set_row(self, index, new_row):
        ''' (Matrix, int, list of float)
        Sets the given row to the value of new_row
        REQ: new_row must be the same length as the original row
        '''
        if (len(new_row) != self._cols):
            raise MatrixIndexError("the new row is longer/shorter than the original row")
        if ((index > self._rows) or (index < 0)):
            raise MatrixIndexError("the given index is out of bounds")

        self._matrix[index] = new_row

    def set_col(self, index, new_col):
        ''' (Matrix, int, list of float)
        Sets the given column to the value of new_col
        REQ: new_col must be the same length as the original column
        '''
        if (len(new_col) != self._rows):
            raise MatrixIndexError("the new column is longer/shorter than the original column")
        if ((index > self._cols) or (index < 0)):
            raise MatrixIndexError("the given index is out of bounds")

        for i in range(0, len(self._matrix)):
            self._matrix[i][index] = new_col[i]
