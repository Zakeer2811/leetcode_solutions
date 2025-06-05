from collections import defaultdict

# Doubly Linked List Node (DLL)
class DLL:
    def __init__(self, key, val):
        self.key = key  # Key of the node
        self.val = val  # Value of the node
        self.freq = 1   # Frequency counter for LFU
        self.prev = None
        self.next = None

# Doubly Linked List to group nodes of same frequency
class DLLGroup:
    def __init__(self):
        self.head = DLL(None, None)  # Dummy head
        self.tail = DLL(None, None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAfterHead(self, node):
        # Insert node just after head (most recently accessed in this frequency group)
        nodeAfterHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nodeAfterHead
        nodeAfterHead.prev = node

    def deleteNode(self, node):
        # Remove a node from its current position in the DLL
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def isEmpty(self):
        # Check if the DLL is empty (only dummy nodes remain)
        return self.head.next == self.tail

    def popLRU(self):
        # Remove the least recently used node in this frequency list (i.e., just before the dummy tail)
        if self.isEmpty():
            return None
        node = self.tail.prev
        self.deleteNode(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum capacity of the cache
        self.map = {}  # Maps key to node for O(1) access
        self.freqMap = defaultdict(DLLGroup)  # Maps frequency to DLL group
        self.minFreq = 0  # Track the minimum frequency in the cache

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1  # Key does not exist in the cache

        node = self.map[key]  # Fetch the node
        self._updateFreq(node)  # Update its frequency as it's accessed
        return node.val  # Return the value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return  # Do nothing if cache capacity is zero

        if key in self.map:
            # If the key already exists, update its value
            node = self.map[key]
            node.val = value
            self._updateFreq(node)  # Since it's accessed/updated, its frequency should increase
        else:
            if len(self.map) == self.capacity:
                # If cache is full, we need to remove the LFU node
                lfuList = self.freqMap[self.minFreq]  # Get the DLL of nodes with minimum frequency
                nodeToRemove = lfuList.popLRU()  # Remove the least recently used node in that frequency group
                del self.map[nodeToRemove.key]  # Remove it from key-node mapping

            # Now insert the new node with frequency = 1
            newNode = DLL(key, value)  # New node starts with frequency 1
            self.map[key] = newNode  # Add it to the map

            # Insert the new node into the DLL that tracks frequency 1
            self.freqMap[1].insertAfterHead(newNode)  
            # Explanation: Insert this node right after the dummy head of freq 1 group,
            # so it's treated as most recently used among freq-1 nodes.

            self.minFreq = 1  
            # Since we added a new node with freq 1, the minimum frequency in the entire cache must now be 1.


    def _updateFreq(self, node):
        freq = node.freq  # Current frequency of the node (before increment)

        self.freqMap[freq].deleteNode(node)  
        # Remove node from its current frequency DLL group (it's about to move to a higher freq group)

        # If this was the only node in the minFreq group, and we removed it,
        # then there are no nodes left at this frequency. So we must update minFreq.
        if freq == self.minFreq and self.freqMap[freq].isEmpty():
            self.minFreq += 1  # Increment minFreq to reflect that current min frequency has no nodes left

        node.freq += 1  # Increase the node's frequency

        # Insert node into the DLL group for its new frequency
        self.freqMap[node.freq].insertAfterHead(node)
        # Explanation: We treat this node as recently accessed in its new freq group,
        # so we insert it right after the dummy head to mark it as most recently used in that group.
