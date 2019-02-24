# Reverse Linked List 
class Solution(object):
    def reverseList(self, head):
        tail=None
        while head:
            t=head.next
            head.next = tail
            tail = head
            head= t
        return tail