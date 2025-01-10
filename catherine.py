def search(self, word):
        """Search for a word in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

def remove(self, word):
        """Remove a word from the Trie."""
        def _remove(node, word, depth):
            if not node:
                return False
            
            if depth == len(word):
                if node.is_word:
                    node.is_word = False
                    return len(node.children) == 0  # If true, delete this node
                return False
            
            char = word[depth]
            if char in node.children:
                should_delete_child = _remove(node.children[char], word, depth + 1)
                if should_delete_child:
                    del node.children[char]
                    return len(node.children) == 0 and not node.is_word
            
            return False
        
        _remove(self.root,word,0)