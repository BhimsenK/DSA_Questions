'''
Leet code : 242. Valid Anagram

Link : https://leetcode.com/problems/valid-anagram/

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Support Video Link : --
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashset = {}  # -> word Count
        hashmap = {}
        for i, j in zip(s, t):
            if i not in hashset:
                hashset[i] = 0
            if j not in hashmap:
                hashmap[j] = 0
            hashset[i] += 1
            hashmap[j] += 1

        # print(hashset)
        # print(hashmap)

        return (hashset == hashmap)

