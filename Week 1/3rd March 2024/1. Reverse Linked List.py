'''
Leet code : 206. Reverse Linked List
Link : https://leetcode.com/problems/reverse-linked-list
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):

        '''As we need to see the previous node for reference so'''
        previous = None

        '''Until there are nodes which are not None'''
        while head:
            '''Here, current is {refering} to same node which is being referred by {head}'''
            current = head

            '''if head is pointing to one node, then this will make it refer to its next node of that node'''
            head = head.next

            '''we are setting reference of {current} to {previous}'''
            current.next = previous

            '''Now {previous} will be refering to {current}'''
            previous = current

        return previous
