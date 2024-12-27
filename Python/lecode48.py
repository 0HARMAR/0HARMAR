class Solution:
    # brute-force
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_cp = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix_cp[n-j-1][i]

    # 
    def rotate (self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # rotate layer num : n//2
        for i in range(n//2):
            for j in range(n-2*i-1):
                temp_num = matrix[i][i+j]
                matrix[i][i+j] = matrix[n-1-j-i][i]
                matrix[n-1-j-i][i] = matrix[n-1-i][n-1-j-i]
                matrix[n-1-i][n-1-j-i] = matrix[i+j][n-1-i]
                matrix[i+j][n-1-i] = temp_num