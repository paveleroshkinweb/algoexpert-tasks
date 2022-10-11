# Time complexity - O(n)
# Space complexity - O(1)
def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    next_list = current.next
    while current and next_list:
        if current.value == next_list.value:
            current.next = next_list.next
            next_list = current.next
        else:
            current = next_list
            next_list = next_list.next
    return linkedList