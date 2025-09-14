# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        getSize=head
        sizePointer=0

        while(getSize):
            sizePointer+=1
            getSize=getSize.next

        makeUpdate=dummy
        updatePointer=0
        while(updatePointer!=sizePointer-n):
            updatePointer+=1
            if(makeUpdate.next):
                makeUpdate=makeUpdate.next
            else:
                break
        if(makeUpdate.next):
            makeUpdate.next=makeUpdate.next.next
            return dummy.next
        else:
            return None
