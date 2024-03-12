'''
Leet code : 125. Valid Palindrome

Link : https://leetcode.com/problems/valid-palindrome/

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Support Video Link : --
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for i in s:
            if i.isalpha() or i.isdigit():
                new += i.lower()

        return (new == new[::-1])

