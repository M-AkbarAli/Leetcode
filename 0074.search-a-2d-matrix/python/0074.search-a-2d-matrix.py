# @leetcode slug=search-a-2d-matrix id=74 qid=74
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        #input: m*n matrix, given in 2nd array form.
        #output: bool, repersents wheter target in matrix or not.
        #Time: O(log(m*n)) -> can do logn checks on every row of the matrix. m is columns, n is rows.
        #No space limit.
        
        #Algo 1: Nested binary search.
        # narrow it down to which row to inspect. 
        # want target > l, and r > target. 
        # l = 1, r = 23.  target > l -> 
        # 

        #what do i need: to get l and r to be the end and start of a row, so i can BST that row only.
        # so i need target to be in the middle of l and r, so l < t < r.
        
        # mid index? not useful here, need to compare the start and ends. 
        #compare to full row values, so if greater than 7, but less than 60, 
        #move r untill less than target. loop cond? while val r > val l. 
        # if r > target, 

        #use middle row
        #set l to 10, and r to 20. 
        #if target > l, and r > target and first index of r == l?

        return True