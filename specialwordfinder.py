
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
        Inherits WordFinder
        Takes file path to text file with words on individual lines
        Works with files that have commented lines and blank lines


        Takes path to file of words where each word is on a single line and turns saves as a list
        Will return random word from list with random() 

        Should log the number of words it read from file on initialization
        >>> swf = SpecialWordFinder('words.txt')
        235886 words read
    """
    def __init__(self, file_path):
        super().__init__(file_path)
    

    def random(self):
        """
            Overrides random() of WordFinder
            Pulls random word from word list and returns it
            If word is either a commented or blank line, it pulls another random word out until success
        """

        word = super().random() 
        while(word == '' or '#' in word):
            word = super().random() 
        return word

