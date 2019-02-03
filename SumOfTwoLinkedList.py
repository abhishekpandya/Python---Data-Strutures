## Linked List add two numbers
# list1 = 1->2->3   list 2 = 3->2->7  output =  4->4->0->1
carry = 0
    cur = ListNode(-1)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=b=0
        if l1 is not None:
            a=l1.val
            l1=l1.next
        if l2 is not None:
            b=l2.val
            l2=l2.next
        if l1 is not None or l2 is not None:
            self.addTwoNumbers(l1,l2)
        s= a+b+self.carry
        self.carry = s//10
        newNode = ListNode(s%10)
        if self.cur.val == -1:
            self.cur = newNode
        else:
            self.cur.next = newNode
            self.cur = newNode
        print(self.cur.val)
        return self.cur