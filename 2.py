# 2. Add Two Numbers
# https://youtu.be/wgFPrzTjm7s?si=sLp5mD-7kvQownTT

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()   # result ListNode
        current = dummy     # Pointer
        carry=0 

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0   #Use zero if val1 is empty/null
            val2=l2.val if l2 else 0

            resVal=val1+val2+carry # result
            carry = resVal // 10   # if there is a new cary, get it
            resVal = resVal % 10   # resVal becomes just the one's place 
            current.next=ListNode(resVal)   # insert into current to return
            current=current.next
            l1= l1.next if l1 else None
            l2= l2.next if l2 else None
        
        return dummy.next
