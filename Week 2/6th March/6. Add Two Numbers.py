'''
Leet code : 2. Add Two Numbers
Link : https://leetcode.com/problems/add-two-numbers/
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Support Video Link : https://youtu.be/wgFPrzTjm7s?si=8Cx4plntuYKN0oBG
'''


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''creating a dummy node so that we can add the sum in it.'''
        dummy = ListNode()
        cur = dummy

        '''This is used to save the carry e.g 7+8 = 15 -> inside node = 5 & in carry = 1.'''
        carry = 0

        '''Untill there are nodes in l1 & l2. Also if those lists are completed and still
        if thre is any value in caryy then for simply adding that carry value in last so '''
        while l1 or l2 or carry:

            '''simply assigning values of both the list if there are nodes else assign 0 instead.
            as there are 2 things in a Node i.e val & next.'''
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry #2+5+0 = 7

            carry = val // 10
            val = val % 10
            ''' 
            e.g
            carry : 7// 10 -> 0
            val : 7// 10 -> 7
            '''

            '''as we have not passed any value while creating the object  of the node, 
            so by default the value passed in the node is "0". So we are passing the val
            in the next node or reference of current which was pointing to the head at first.'''
            cur.next = ListNode(val)

            # update ptrs
            '''Now we are moving the cursor of "cur" from "cur" to "cur.next" i.e next node.'''
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        '''if we return only "dummy", then it will give correct response but there will be "0" at 
         first position so we are excluding that 0.'''
        return dummy.next
