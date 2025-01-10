# Group 2 Tries Dictionary Application
## Contributors
1. Samuel Gicheha - SCT212-0118/2022
2. Geoffrey Kirumba - SCT212-0137/2022
3. Bridget Wanjiru - SCT212-0466/2022
4. Catherine Mumbi - SCT212-0721/2022
5. Felister Njeri - SCT212-0720/2022

## Overview
This application is a dictionary with autocomplete functionality. It uses the Trie data structure to efficiently store and retrieve words. The graphical user interface (GUI) is built with the tkinter library.

## Features
1. Add Words: Users can add new words to the dictionary
2. Check words: Users can check if a word exists in the dictionary
3. Remove words: Users can remove words from the dictionary
4. Autocomplete Suggestions: As users type, the application suggests words that start with the entered prefix

## Code Structure
The application consists of the following main components:

### 1. TrieNode Class
This class represents a single node in the Trie. Each node contains:
- children: A dictionary mapping characters to their corresponding child nodes.
- is_word: A boolean indicating whether the node marks the end of a valid word.
  
### 2. Trie Class
This class implements the Trie data structure with the following methods:
- insert(word): Inserts a word into the Trie.
- search(word): Searches for a word in the Trie and returns True if it exists, otherwise False.
- remove(word): Removes a word from the Trie.
- suggest(prefix): Returns a list of words that start with the given prefix.
- _collect_words(node, prefix, suggestions): A helper function to collect words from the Trie.
  
### 3. DictionaryApp Class
This class creates the GUI for the application and handles user interactions. It includes:
- __init__(root): Initializes the application and creates GUI components.
- create_widgets(): Sets up the GUI elements such as entry fields, buttons, and listboxes.
- on_key_release(event): Updates suggestions based on user input.
- add_word(): Adds a word to the Trie and displays a success message.
- check_word(): Checks if a word exists in the Trie and displays the result.
- remove_word(): Removes a word from the Trie and displays a success message.
  
### 4. Main Execution Block
The application starts by creating a Tkinter window and initializing the DictionaryApp.

## Usage
### 1. Adding a Word
- Type a word in the input field and click the "Add Word" button. A success message will confirm the addition.
  
### 2. Checking a Word
- Type a word in the input field and click the "Check Word" button. A message will indicate whether the word exists in the dictionary.
  
#3# 3. Removing a Word
- Type a word in the input field and click the "Remove Word" button. A success message will confirm the removal.
  
### 4. Autocomplete Suggestions
- As you type in the input field, suggestions will appear in the listbox below.
