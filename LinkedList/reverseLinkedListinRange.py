# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        before_reverse = dummy
    
        for _ in range(left - 1):
            before_reverse = before_reverse.next
        
        current = before_reverse.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = before_reverse.next
            before_reverse.next = temp
        return dummy.next
        
