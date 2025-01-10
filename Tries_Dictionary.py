class DictionaryApp:
    def _init_(self, root):
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