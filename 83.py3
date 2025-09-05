# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        temp=head
        while(temp):
            seen.add(temp.val)
            if(temp.next is None):         # Identify last ListNode
                if(temp.val in seen):      # Check last ListNode isn't a dupe
                    temp.next=None
                break
            if(temp.next.val in seen):      # Look ahead
                temp.next=temp.next.next    # Edit pointers
            else:
                temp=temp.next
        return head
