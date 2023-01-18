class Solution:
    def minimumTotal(self, triangle: List[List[int]]):
        for level in range(len(triangle)-2,-1,-1):
            for i in range(level+1):
                triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
        return triangle[0][0]

'''
At each cell of the triangle, we could have moved here from the below level in 2 ways, either from -
the same index i in below row, or
the index i+1.
And again, we will choose the minimum of these two to arrive at the optimal solution. Finally at last, we will reach at triangle[0][0], which will hold the optimal (minimum) sum of path.
'''
