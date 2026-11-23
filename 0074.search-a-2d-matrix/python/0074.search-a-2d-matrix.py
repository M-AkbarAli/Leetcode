# @leetcode slug=search-a-2d-matrix id=74 qid=74
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        #Algo:
        # lo = m[0] , high = len(matrix) -1           // hurdle one, how to dynamically find rows in a matrix.
        # hi >= lo
        # mid = hi + low / 2.
        # if target > mid, lo = mid + 1
        # if target < mid, hi = mid - 1.
        # if target is in row of mid, then BST. 

        lo = 0
        hi = len(matrix) - 1

        while hi >= lo:
            mid = (hi + lo) // 2
            a = matrix[mid][0]
            b = matrix[mid][len(matrix[mid])- 1]
            
            if a <= target <= b:
                l = 0
                r = len(matrix[mid])- 1
                middle = (r + l) // 2
                while r >= l:
                    if target == matrix[mid][middle]:
                        return True
                    elif target > matrix[mid][middle]:
                        l = middle + 1
                    else:
                        r = middle - 1
            elif target > b:
                lo = mid + 1
            else:
                hi = mid - 1


        return False