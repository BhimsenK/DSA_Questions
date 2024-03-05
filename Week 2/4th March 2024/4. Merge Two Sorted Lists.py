'''
Leet code : 21. Merge Two Sorted Lists
Link : https://leetcode.com/problems/merge-two-sorted-lists/
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Support Video Link : https://youtu.be/XIdigk956u0?si=wFUpIWbIEVFUsLKr
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        '''Creating new object/ node named as dummy.'''
        dummy = ListNode()
        temp  = dummy

        while list1 and list2:
            '''If 1st values of 1st list is less than 1st value of 2nd list, then we are adding 1st node of 1st list.
             and vice versa.'''
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next


        '''we were using "while list1 and list2:" this condition above, so if either of list
         gets empty then we are simply checking if other list is remaining or not.
         If yes, then we are appending all the values of it directly to the node as they
         are already sorted.'''
        if list1:
            temp.next=list1
        elif list2:
            temp.next=list2


        return dummy.next

    '''Q. Why are we returning dummy.next and why not only dummy ?
    > With dummy : Output: [1,1,2,3,4,4]
    > Without dummy : Output: [0,1,1,2,3,4,4]

    we are creating dummy using "dummy = ListNode()". Here you can see, we
     are not passing any parameter in the ListNode() while creating the object.
     So it will be taking head as 0 & next as None by default as we are delaring
     these values inside the __init__() of class ListNode.'''

