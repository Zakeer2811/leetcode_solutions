class DLL:
    def __init__(self, key, val):
        self.key = key  # Key of the node
        self.val = val  # Value associated with the key
        self.prev = None  # Pointer to the previous node in DLL
        self.next = None  # Pointer to the next node in DLL

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum number of entries allowed in the cache
        self.map = {}  # Dictionary to store key-node mapping for O(1) access

        # Create dummy head and tail nodes to simplify insertion and deletion logic
        self.dhead = DLL(-1, -1)
        self.dtail = DLL(-1, -1)
        self.dhead.next = self.dtail  # Initially head is connected to tail
        self.dtail.prev = self.dhead  # Tail is connected back to head

    # Helper function to insert a node right after the dummy head
    # This position indicates the most recently used item
    def insertAfterHead(self, node):
        nodeAfterHead = self.dhead.next
        self.dhead.next = node
        node.prev = self.dhead
        node.next = nodeAfterHead
        nodeAfterHead.prev = node

    # Helper function to remove a node from its current position in the DLL
    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # Retrieve value from cache
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1  # Key not found in cache

        node = self.map[key]  # Get the node
        self.deleteNode(node)  # Remove it from its current position
        self.insertAfterHead(node)  # Move it to the most recently used position
        return node.val  # Return the value associated with the key

    # Add or update a key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # If key exists, update the value and move node to front
            node = self.map[key]
            node.val = value  # Update value
            self.deleteNode(node)  # Remove from current position
            self.insertAfterHead(node)  # Insert at the front
        else:
            # If key does not exist and capacity is full, remove LRU node
            if len(self.map) == self.capacity:
                LRUNode = self.dtail.prev  # Node before dummy tail is least recently used
                self.deleteNode(LRUNode)  # Remove it from the DLL
                del self.map[LRUNode.key]  # Remove its entry from the map

            # Create a new node and insert it at the front
            newNode = DLL(key, value)
            self.map[key] = newNode  # Add to map
            self.insertAfterHead(newNode)  # Add to DLL after dummy head
