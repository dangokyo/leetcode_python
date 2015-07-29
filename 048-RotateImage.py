class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
    	length = len(matrix);
    	if(length==0):
    		return;
    	
    	for i in range(0, length-1):
    		for j in range(0, length-i-1):
    			t = matrix[i][j];
    			matrix[i][j] = matrix[length-1-j][length-1-i];
    			matrix[length-1-j][length-1-i] = t;
    	
    	for i in range(0, length/2):
    		for j in range(0, length):
    			t = matrix[i][j];
    			matrix[i][j] = matrix[length-1-i][j];
    			matrix[length-1-i][j] = t;
    	return;
    	
matrix = [[1,2,3], [4,5,6], [7,8,9]];
slt= Solution();
slt.rotate(matrix);
print(matrix)