# Time complexity - O(n)
# Space complexity - O(1)
def removeKthNodeFromEnd(head, k):
    pointer1 = head
    pointer2 = head
    for _ in range(k):
        pointer2 = pointer2.next
    if pointer2 is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while pointer2.next is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    pointer1.next = pointer1.next.next