# Time complexity - O(max(n, m))
# Space complexity - O(max(n, m))
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sum_head = current = None
    remainer = 0
    while linkedListOne or linkedListTwo :
        next1 = linkedListOne.value if linkedListOne else 0
        next2 = linkedListTwo.value if linkedListTwo else 0
        new_value = next1 + next2 + remainer
        whole_part = new_value % 10
        remainer = new_value // 10
        new_node = LinkedList(whole_part)
        if sum_head is None:
            sum_head = new_node
            current = new_node
        else:
            current.next = new_node
            current = current.next
        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None
    if remainer:
        current.next = LinkedList(remainer)
    return sum_head