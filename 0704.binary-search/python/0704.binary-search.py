# @leetcode slug=binary-search id=704 qid=792
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        #output: integer, (-1) if not present, else return index.
        #all integers in nums are unique

        #Algorithm: Binary Search (Im not writing it out legit in question name)
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
            
        return -1