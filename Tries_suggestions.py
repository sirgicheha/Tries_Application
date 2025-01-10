def suggest(self, prefix):
        """Suggest all words in the Trie that start with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No suggestions if prefix not found
            node = node.children[char]
        
        suggestions = []
        self._collect_words(node, prefix, suggestions)
        return suggestions

def _collect_words(self, node, prefix, suggestions):
        """Helper function to collect words from the Trie."""
        if node.is_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char,suggestions)