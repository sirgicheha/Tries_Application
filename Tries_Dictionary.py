import tkinter as tk
from tkinter import Listbox, StringVar, messagebox

# GUI buttons implementation
def on_key_release(self, event):
        """Handle key release event to update suggestions."""
        prefix = self.word_var.get()
        suggestions = self.trie.suggest(prefix)
        
        # Clear the current suggestions
        self.suggestion_listbox.delete(0, tk.END)
        
        # Insert new suggestions
        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def add_word(self):
        """Add a word to the Trie."""
        word = self.word_var.get().strip()
        if word:
            self.trie.insert(word)
            messagebox.showinfo("Success", f"'{word}' has been added to the dictionary.")
        else:
            messagebox.showwarning("Input Error", "Please enter a word to add.")

    def check_word(self):
        """Check if a word exists in the Trie."""
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
        """Remove a word from the Trie."""
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