# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iterative solution
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
# O(n) runtime of complexity, n is the number of nodes in the ll
# O(1) memory complexity, because it uses just two pointers regardless of the input ll

# recursive solution (less effective, cause recursive call stack is O(n) memory)
class Solution(object):
    def reverseList(self, head):
        def reverse(curr, prev):
            if curr is None:
                return prev
            else:
                nxt = curr.next
                curr.next = prev
                return reverse(nxt, curr)

        return reverse(head, None)