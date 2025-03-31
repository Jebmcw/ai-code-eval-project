import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the modules
from Solutions.human_solution_1 import reverse_list as human_reverse
from Solutions.ai_solution_1 import reverse_list as ai_reverse

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestReverseList(unittest.TestCase):
    def test_human_solution(self):
        lst = build_linked_list([1, 2, 3])
        reversed_lst = human_reverse(lst)
        self.assertEqual(linked_list_to_list(reversed_lst), [3, 2, 1])

    def test_ai_solution(self):
        lst = build_linked_list([1, 2, 3])
        reversed_lst = ai_reverse(lst)
        self.assertEqual(linked_list_to_list(reversed_lst), [3, 2, 1])

if __name__ == "__main__":
    unittest.main()
