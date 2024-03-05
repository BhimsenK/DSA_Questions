'''
Leet code : 141. Linked List Cycle
Link : https://leetcode.com/problems/linked-list-cycle/
Input: head = [3,2,0,-4], pos = 1
Output: true

Support Video Link : https://youtu.be/gBTe7lFR3vc?si=S43bwiGHNMjpx3V6
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''Having 2 nodes pointing @head'''
        slow = fast = head

        '''Slow = 1, fast = 2 (will move ahead with mentioned nodes.) thats why checking if fast & its next node is
        None or not.'''
        while fast and fast.next:
            '''slow will be moving 1 node ahead while fast is moving 2 nodes every time. 
            if they connected at some point, it means its a circle. and if fast found the None reference it
            means there is no cycle.'''
            slow, fast = slow.next, fast.next.next
            # fast = fast.next.next

            if slow == fast:
                return True


        return False