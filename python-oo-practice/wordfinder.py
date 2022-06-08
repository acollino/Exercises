"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    Class that creates a list of words from a file and can return random
    words from that list
    """

    def __init__(self, filepath):
        """Create an instance of WordFinder from a filepath str"""
        self.filepath = filepath
        self.word_list = WordFinder.generate_word_list(filepath)
        print(f"{len(self.word_list)} words read")

    @classmethod
    def generate_word_list(cls, filepath):
        """
        generate a list of strings from a filepath, one string per
        line in the file
        """
        with open(filepath) as word_file:
            words = [line.strip() for line in word_file]
            return words
        
    def random(self):
        """return a random word from the word list"""
        return choice(self.word_list)
