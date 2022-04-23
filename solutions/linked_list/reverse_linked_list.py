# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional
from solutions.linked_list.list_node import ListNode


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None
    if current is None or current.next is None:
        return current
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
