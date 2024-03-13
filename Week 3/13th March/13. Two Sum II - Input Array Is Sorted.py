'''
Leet code : 167. Two Sum II - Input Array Is Sorted

Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Support Video Link : --
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #2 pointer technique

        '''Setting 2 pointers, one at starting and second at the end.'''
        Left, Right = 0, len(numbers) - 1
        new = []

        while Left < Right:
            sum = numbers[Left] + numbers[Right]

            '''As its a sorted list, so If sum is greater than target, then ofcourse there are greter nums
            at right side. So we need to subtract 1 from right. and if Sum is smaller than target, then
            add 1 in left to move it to right.'''

            if sum > target:
                Right -= 1
            elif sum < target:
                Left += 1
            else:
                # Left += 1
                # Right += 1
                '''Adding values in list i.e new[].'''
                new.extend([Left + 1, Right + 1])
                # new.append(Left)
                # new.append(Right)
                # # return [Left+1, Right +1]
                break
        return new
