'''
Leet code : 217. Contains Duplicate
Link : https://leetcode.com/problems/contains-duplicate/

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Support Video Link : https://youtu.be/wjYnzkAhcNk?si=kMvfC9gXS4FrLaEe
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

'''
e.g : 
nums = [1, 5, 2, 3,1]

Hashset : set()
Hashset : {1}
Hashset : {1, 5}
Hashset : {1, 2, 5}
Hashset : {1, 2, 3, 5}
'''
