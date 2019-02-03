## Returns intersection point of 2 linked list

def findMergeNode(head1, head2):
    if head1 and head2 is None:
            return None
    a=head1
    b=head2
    while a is not b:
        if a:
            a=a.next
        else:
            a=headB
        if b:
            b=b.next
        else:
            b=headA
    return a