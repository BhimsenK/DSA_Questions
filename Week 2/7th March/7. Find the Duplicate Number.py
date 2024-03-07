'''
Leet code : 287. Find the Duplicate Number
Link : https://leetcode.com/problems/find-the-duplicate-number/

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Support Video Link : https://youtu.be/wjYnzkAhcNk?si=kMvfC9gXS4FrLaEe
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # # Find the entrance to the cycle (duplicate number)
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

'''If you want to see the output of this for testcases, please checkout the "output flow.txt" '''


