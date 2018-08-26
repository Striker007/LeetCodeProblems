class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = Solution6()
        return s.mergeTwoLists(l1, l2)


class Solution6:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        
        if not l2:
            return l1

        if not l1 and not l2:
            return None
        
        node = guard_node = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        
        if l1 or l2:
            node.next = l1 or l2
        
        return guard_node.next


class Solution5:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        head = ListNode(0)
        tail = head
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
            tail.next = None
        
        if l1 != None:
            tail.next = l1
        elif l2 != None:
            tail.next = l2
        
        return head.next


class Solution4:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        
        if not l2:
            return l1

        r = []
        while l1 or l2:

            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    r.append(l1.val)
                    l1 = l1.next
                elif l1.val > l2.val:
                    r.append(l2.val)
                    l2 = l2.next
                else:
                    r.append(l1.val)
                    r.append(l2.val)
                    l1 = l1.next
                    l2 = l2.next
                    
            elif l1 is not None:
                r.append(l1.val)
                l1 = l1.next
            elif l2 is not None:
                r.append(l2.val)
                l2 = l2.next
                
            else:
                break
                
        return r


class Solution3:
    def mergeTwoLists(self, l1, l2):
        r = []
        while l1 or l2:

            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    r.append(l1.val)
                    l1 = l1.next
                elif l1.val > l2.val:
                    r.append(l2.val)
                    l2 = l2.next
                else:
                    r.append(l1.val)
                    r.append(l2.val)
                    l1 = l1.next
                    l2 = l2.next
                    
            elif l1 is not None:
                r.append(l1.val)
                l1 = l1.next
            elif l2 is not None:
                r.append(l2.val)
                l2 = l2.next
                
            else:
                break
                
        return r


class Solution2:
    def mergeTwoLists(self, l1, l2):
 
        l1_converted = []
        l2_converted = []
 
        while l1:
            l1_converted.append(l1.val)
            if l1.next is not None:
                l1 = l1.next
            else:
                l1 = None
                
        while l2:
            l2_converted.append(l2.val)
            if l2.next is not None:
                l2 = l2.next
            else:
                l2 = None
        
        l3 = l1_converted + l2_converted
        l3.sort()

        return l3


class Solution1:
    def mergeTwoLists(self, l1, l2):
        l3 = []

        while l1 or l2:
            if l1 is not None:
                l3.append(l1.val)
                if l1.next is not None:
                    l1 = l1.next
                else:
                    l1 = None 

            if l2 is not None:
                l3.append(l2.val)
                if l2.next is not None:
                    l2 = l2.next
                else:
                    l2 = None 

        l3.sort()
        
        return l3
