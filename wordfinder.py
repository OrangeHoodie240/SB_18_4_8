from random import randint

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
        Takes path to file of words where each word is on a single line and turns saves as a list
        Will return random word from list with random() 

        Should log the number of words it read from file on initialization
        >>> wf = WordFinder('words.txt')
        235886 words read
    """ 

    def __init__(self, file_path):
        self.words = WordFinder.get_words(file_path)
        self.length = len(self.words)
        print(f'{self.length} words read')
    
    @staticmethod
    def get_words(file_path):
        """
            Takes path to file with a single word on each line
            Returns list of those words
        """
        words = []
        with open(file_path) as f:
            for line in f:
                words.append(line.strip())
        return words 

    def random(self):
        """
            Returns random word from list of words
        """
        i = randint(0, self.length-1)
        return self.words[i]