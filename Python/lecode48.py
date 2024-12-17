class Solution:
    # brute-force
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_cp = copy.deepcopy(matrix)
        matrix_dimension = len(matrix)
        for i in range(matrix_dimension):
            for j in range(matrix_dimension):
                matrix[i][j] = matrix_cp[matrix_dimension-j-1][i]

    # 
    def rotate (self, matrix: List[List[int]]) -> None:
        