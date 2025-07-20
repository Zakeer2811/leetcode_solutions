from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.name = ""
        self.duplicate = False  # Mark duplicate subtree

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Step 1: Build the Trie
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = TrieNode()
                    node.children[name].name = name
                node = node.children[name]

        # Step 2: Post-order serialization
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            items = []
            for child in sorted(node.children):  # sort to ensure consistent serialization
                ser = serialize(node.children[child])
                items.append(f"{child}({ser})")
            rep = "".join(items)
            serial_map[rep].append(node)
            return rep

        serialize(root)

        # Step 3: Mark duplicates
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.duplicate = True

        # Step 4: DFS to collect valid paths
        res = []

        def dfs(node, path):
            for name, child in node.children.items():
                if not child.duplicate:
                    new_path = path + [name]
                    res.append(new_path)
                    dfs(child, new_path)

        dfs(root, [])
        return res
