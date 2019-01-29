class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        current = head
        _next = head.next  
            
        while _next:

            if current.val == _next.val:
                if _next.next:
                    current.next = _next.next
                else:
                    current.next = None
            else:
                current = current.next
     
            if current and current.next:
                _next = current.next
            else:
                _next = None

        return head
