# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        prev=None
        #to go to the mmiddle while revesing till it get there
        while fast and fast.next:
            fast=fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        res=0
        while slow:
            #Finding maximum pair sum of corresponding nodes
            res=max(res,prev.val+slow.val)
            prev=prev.next
            slow=slow.next
        return res
