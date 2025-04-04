# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if slow == None:
            return None
        fast = head.next
        while fast != None and fast.next != None and slow != fast:
            fast = fast.next.next
            slow = slow.next
        if fast == None or fast.next == None or slow != fast:
            return None

        k = 1
        fast = fast.next
        while slow != fast:
            fast = fast.next
            k += 1
        fast = head
        slow = head
        while k > 0:
            k -=1
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow



        # nodes = set()
        # while head is not None:
        #     if head in nodes:
        #         return head
        #     nodes.add(head)
        #     head = head.next
        # return None
        
# runtime: O(n)
# spacetime: O(n) with set and O(1) with floyd's algo
