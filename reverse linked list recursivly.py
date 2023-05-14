
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        def rec(prev,cur):
            if not cur:
                return prev
            tail= rec(cur,cur.next)

            cur.next =prev
            return tail
        return rec(None,head)
