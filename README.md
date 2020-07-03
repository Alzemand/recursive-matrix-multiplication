


  <h3 align="center">Recursive square matrix multiplication in Python using index calculations</h3>


The following algorithm for square matrix multiplication is from the Introduction to Algorithms, Third edition:

```sh
SQUARE-MATRIX-MULTIPLY-RECURSIVE (A, B)
	n = A.rows
	let C be a new n x n matrix
	if n == 1
		c11 = a11 x b1
	else partition A, B, and C as in equations (4.9)
		C11 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11, B11)
		    + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12, B21)       
		C12 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11, B12)
	        + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12, B22)        
		C21 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21, B11)
	        + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22, B21)        
		C22 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21, B12)
	        + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22, B22)
	    return C
```
The divide-and-conquer algorithm to compute the matrix product C = A . B, with the assumption that n is an exact power of 2 in each of the n x n matrices. 

In the following implementation of the divide-and-conquer algorithm I have used the partitioning of the matrices using index calculations.