# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        total_nodes = nodes = 0
        node = head
        while node.next:
            total_nodes += 1
            node = node.next
        
        node = head
        while nodes < total_nodes/2:
            node = node.next
            nodes += 1
        return node

if __name__ == "__main__":
    node5 = ListNode(6)
    node4 = ListNode(5, node5)
    node3 = ListNode(4, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(2, node2)
    head = ListNode(1, node1)
    print(Solution().middleNode(head).val)
