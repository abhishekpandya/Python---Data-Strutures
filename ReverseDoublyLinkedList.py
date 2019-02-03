## Reverse doubly linked list

def reverse(head):
    temp=None
    p=head
    while p is not None: 
        temp = p.prev  
        p.prev = p.next
        p.next = temp 
        p = p.prev
    if temp is not None: 
        head = temp.prev  
    return head