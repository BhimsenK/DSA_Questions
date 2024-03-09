'''
Leet code : 1. Two Sum
Link : https://leetcode.com/problems/contains-duplicate/

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Support Video Link : https://youtu.be/UXDSeD9mN-k?si=qc57lEqQKgvtQA-k
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashmap:
                return (hashmap[diff], i)

            hashmap[n] = i

