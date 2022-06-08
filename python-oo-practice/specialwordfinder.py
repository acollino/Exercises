"""
Special Word Finder: finds random words from a dictionary, ignoring
any blank lines or comments.
"""
from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """
    Class that creates a list of words from a file while ignoring empty lines
    or lines that are commented with '#' and can return random words from 
    that list.

    >>> swf = SpecialWordFinder("test.txt")
    3 words read

    >>> swf.random() in ['print', 'these', 'words']
    True

    >>> swf.random() in ['print', 'these', 'words']
    True

    >>> swf.random() in ['print', 'these', 'words']
    True
    """

    def __init__(self, filepath):
        """Create an instance of SpecialWordFinder from a filepath str"""
        super().__init__(filepath)

    def generate_word_list(self):
        """
        generate a list of non-empty, non-commented strings from a filepath, 
        one string per line in the file
        """
        with open(self.filepath) as word_file:
            words = [line.strip() for line in word_file if not line.startswith(("#", "\n"))]
            return words
