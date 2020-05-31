# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, obj):
        assert isinstance(obj, self.__class__)
        if (self.next and not obj.next) or (obj.next and not self.next):
            return False
        if self.next:
            return self.next == obj.next
        return self.val == obj.val


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_number = self.convert_listnode_to_number(l1)
        second_number = self.convert_listnode_to_number(l2)
        result_number = first_number + second_number
        result_listnode = self.convert_number_to_listnode(result_number)
        return result_listnode

    def convert_listnode_to_number(self, listnode: ListNode):
        tmp_listnode = listnode
        num_as_string = str(tmp_listnode.val)
        while tmp_listnode.next:
            tmp_listnode = tmp_listnode.next
            num_as_string += str(tmp_listnode.val)
        reversed_num_as_string = num_as_string[::-1]
        return int(reversed_num_as_string)

    def convert_number_to_listnode(self, num) -> ListNode:
        num_as_string = str(num)  # [::-1]
        result_node = None
        for char in num_as_string:
            result_node = ListNode(int(char), result_node)
        return result_node


def test_listnode_equals():
    assert ListNode() == ListNode()
    assert ListNode(1) == ListNode(1)
    assert ListNode(1) != ListNode(2)

    num_123 = ListNode(3, ListNode(2, ListNode(1)))
    num_321 = ListNode(1, ListNode(2, ListNode(3)))
    num_123_another = ListNode(3, ListNode(2, ListNode(1)))
    assert num_123 == num_123_another
    assert num_123 != num_321

def test_convert_listnode_to_number():
    sol = Solution()
    assert sol.convert_listnode_to_number(ListNode()) == 0
    assert sol.convert_listnode_to_number(ListNode(1)) == 1
    assert sol.convert_listnode_to_number(ListNode(2, ListNode(1))) == 12
    assert sol.convert_listnode_to_number(ListNode(2, ListNode(1, ListNode(3)))) != 12
    assert sol.convert_listnode_to_number(ListNode(2, ListNode(1, ListNode(3)))) == 312

def test_convert_number_to_listnode():
    sol = Solution()
    assert sol.convert_number_to_listnode(0) == ListNode()
    assert sol.convert_number_to_listnode(1) == ListNode(1)
    assert sol.convert_number_to_listnode(12) == ListNode(2, ListNode(1))
    assert sol.convert_number_to_listnode(312) == ListNode(2, ListNode(1, ListNode(3)))

def test_ok1():
    assert Solution().addTwoNumbers(ListNode(), ListNode()) == Solution().convert_number_to_listnode(0)
    assert Solution().addTwoNumbers(ListNode(1), ListNode()) == Solution().convert_number_to_listnode(1)
    assert Solution().addTwoNumbers(ListNode(1), ListNode(3)) == Solution().convert_number_to_listnode(4)
    assert Solution().addTwoNumbers(ListNode(2, ListNode(1)), ListNode(3)) == Solution().convert_number_to_listnode(15)
    assert Solution().addTwoNumbers(ListNode(2, ListNode(1)), ListNode(0, ListNode(0, ListNode(1)))) == Solution().convert_number_to_listnode(112)

    num_342 = ListNode(2, ListNode(4, ListNode(3)))
    num_465 = ListNode(5, ListNode(6, ListNode(4)))
    num_807 = ListNode(7, ListNode(0, ListNode(8)))
    assert Solution().addTwoNumbers(num_342, num_465) == num_807

