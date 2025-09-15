# 2807. Insert Greatest Common Divisors in Linked List

import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        current = dummy

        while current.next:
            new = gcd(current.val,current.next.val)
            newNode = ListNode(new) # node on it's own
            newNode.next = current.next # add pointer to next original val
            current.next = newNode     # add pointer from original to new
            current = current.next.next #skip the newly added node to process next from original
        return head # return the original reference to the head
