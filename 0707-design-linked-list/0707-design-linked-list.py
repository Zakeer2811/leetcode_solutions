class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        # Initialize the linked list with a dummy head node
        self.head = ListNode()  # This dummy node simplifies edge case handling
        self.size = 0  # Keep track of the size of the linked list

    def get(self, index: int) -> int:
        # Check if the index is valid
        if index < 0 or index >= self.size:
            return -1  # Invalid index
        current = self.head
        for _ in range(index + 1):  # Traverse to the node at the given index
            current = current.next
        return current.val  # Return the value of the node at the index

    def addAtHead(self, val: int) -> None:
        # Add a node at the head of the list
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # Add a node at the tail of the list
        current = self.head
        while current.next:
            current = current.next
        new_node = ListNode(val)
        current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Add a node at the given index
        if index < 0 or index > self.size:  # Invalid index
            return
        current = self.head
        for _ in range(index):  # Traverse to the node just before the desired index
            current = current.next
        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # Delete the node at the given index
        if index < 0 or index >= self.size:  # Invalid index
            return
        current = self.head
        for _ in range(index):  # Traverse to the node just before the desired index
            current = current.next
        current.next = current.next.next  # Remove the node by skipping it
        self.size -= 1

