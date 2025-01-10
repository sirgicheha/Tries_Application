import tkinter as tk
from tkinter import Listbox, StringVar, messagebox

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

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
        
        _remove(self.root, word, 0)

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
            self._collect_words(child_node, prefix + char, suggestions)

class DictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary with Autocomplete")
        
        self.trie = Trie()
        
        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        """Create the GUI components."""
        # Entry for word input
        self.word_var = StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.word_var)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.on_key_release)  # Corrected line

        # Listbox to display suggestions
        self.suggestion_listbox = Listbox(self.root)
        self.suggestion_listbox.pack(pady=10)

        # Buttons for dictionary operations
        self.add_button = tk.Button(self.root, text="Add Word", command=self.add_word)
        self.add_button.pack(pady=5)

        self.check_button = tk.Button(self.root, text="Check Word", command=self.check_word)
        self.check_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Word", command=self.remove_word)
        self.remove_button.pack(pady=5)

# GUI buttons implementation
    def on_key_release  (self, event):
        """Handle key release event to update suggestions."""
        prefix = self.word_var.get()
        suggestions = self.trie.suggest(prefix)
        
        # Clear the current suggestions
        self.suggestion_listbox.delete(0, tk.END)
        
        # Insert new suggestions
        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def add_word(self):
        # Add a word to the Trie
        word = self.word_var.get().strip()
        if word:
            self.trie.insert(word)
            messagebox.showinfo("Success", f"'{word}' has been added to the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to add.")

    def check_word(self):
        # Check if a word exists in the Trie
        word = self.word_var.get().strip()
        if word:
            exists = self.trie.search(word)
            if exists:
                messagebox.showinfo("Check Word", f"'{word}' exists in the dictionary.")
            else:
                messagebox.showinfo("Check Word", f"'{word}' does not exist in the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to check.")

    def remove_word(self): 
        # Remove a word from the Trie
        word = self.word_var.get().strip()
        if word:
            self.trie.remove(word)
            messagebox.showinfo("Success", f"'{word}' has been removed from the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
