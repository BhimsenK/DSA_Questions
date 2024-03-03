'''
Leet code : 876. Middle of the Linked List
Link : https://leetcode.com/problems/middle-of-the-linked-list
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Support Video Link : https://youtu.be/FTjQcajqgwA?si=NYmM5Wbsex-NG7xx
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        count = 0
        start = head

        '''FOA we need count the length of the LL'''
        while start is not None:
            count += 1
            start = start.next

        #print(count)

        '''Fetching middle count of the LL'''
        middle = count // 2
        print(middle)


        '''here, we are working on the indexing of the LL.
        As we have the middle count so we just iterate the while loop
        until we get the middle count match.
        Once we got the match, we are simply returning that node.'''
        temp = head
        current = 0
        while temp is not None :
            if current == middle:
                return temp
            else:
                current += 1
                temp = temp.next
        return None