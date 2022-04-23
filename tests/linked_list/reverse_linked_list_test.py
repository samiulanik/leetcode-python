from solutions.linked_list import reverse_linked_list
from solutions.linked_list.list_node import ListNode


def test_happy_path():
    values = [1, 2, 3, 4, 5]
    size = len(values)
    values_ll = []

    for i in values:
        values_ll.append(ListNode(i))

    for i in range(size):
        if i >= size - 1:
            break
        values_ll[i].next = values_ll[i + 1]

    reversed_head = reverse_linked_list.reverseList(values_ll[0])
    reversed_output = []
    current = reversed_head
    while current is not None:
        reversed_output.append(current.val)
        current = current.next

    assert reversed_output == list(reversed(values))
