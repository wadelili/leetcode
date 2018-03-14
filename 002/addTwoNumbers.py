#!python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = None
        last_node = None
        carry = 0
        this_node1 = l1
        this_node2 = l2
        while this_node1 is not None or this_node2 is not None:
            val1 = 0 if this_node1 is None else this_node1.val
            val2 = 0 if this_node2 is None else this_node2.val
            this_val = val1 + val2 + carry
            carry = (0, 1)[this_val > 9]

            # first node
            if last_node is None:
                node = ListNode(this_val % 10)
                last_node = node
            # other node
            else:
                last_node.next = ListNode(this_val % 10)
                last_node = last_node.next

            this_node1 = None if this_node1 is None else this_node1.next
            this_node2 = None if this_node2 is None else this_node2.next

        if carry > 0:
            last_node.next = ListNode(carry)

        return node