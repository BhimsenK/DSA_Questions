'''
Leet code : Reverse a Linked List in groups of given size
Link : https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

Input: LinkedList: 1->2->2->4->5->6->7->8
       K = 4
Output: 4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.

Support Video Link : 1. https://youtu.be/0FKGrkkTb0U?si=PDwikd_QMpCxU1rP - Coding Crane
                     2. https://youtu.be/fi2vh0nQLi0?si=yILsbo2A289SFQ5j - CodeHelp - by Babbar
'''



"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        # Code here
        '''if the LL is empty then will return None.'''
        if head is None:
            return None

        pre = None  #just to get the previous node reference
        count = 0
        curr = head

        '''The logic will be same as reversing the LL. But  here we need to add one condition which will check
        whether the {curr} which we are now refering to {head} is not empty <and> the count is less than {k} 
        or not.'''
        while (curr != None and count < k):
            '''we are saving the reference of curr.next into {next}.  '''
            next = curr.next

            '''now, {curr.next} means the reference saved in {curr} we are assigning to {pre}.'''
            curr.next = pre

            '''Now this {pre} will be refering to {curr}'''
            pre = curr

            '''and same way, now {curr} will be refering to {next} in which we already saved the next node
            of {curr}'''
            curr = next
            count += 1

        '''Once the count of {k} is matched, then it will come outof the loop and again do the same process
        for rest of the nodes. But before that we need to assign the {next} as a {head} while passing
        / calling the reverse().'''
        if next != None:
            head.next = self.reverse(next, k)

        return pre


#Driver code ...