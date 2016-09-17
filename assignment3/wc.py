from sys import argv

class WordCount:
    """A script used to determine number of lines, words and chars in files.

    The purpose of this class is to read the entire contents of files and count each
    line separated by a new line (\\n), each word separated by whitespace (' ') or
    a new line (\\n) and each char (byte) in the text.

    Attributes:
        filename: A list of filenames.
        line_counter: A list of number of lines in separate files. The position of a specific file
            is the same as in filename.
        word_counter: A list of number of words in separate files.
        char_counter: A list of number of bytes in separate files.
    """

    def __init__(self, filename):
        """Constructor for class WordCount.

        The constructor initializes the lists filename, line_counter, word_counter and char_counter.

        Args:
            filename: A list of filenames.
        """
        self.filename = filename
        self.line_counter = []
        self.word_counter = []
        self.char_counter = []

    def __call__(self):
        """Calling function for class WordCount.

        The calling function iterates through the list of filenames in the list filename and tries
        to open these strings with the built-in open-function for reading. If the file is
        successfully opened __call__ calls the private function _count_bytes with the file-object.
        It then proceeds to output the number of lines, words and characters in the file.

        If the specified filename isn't a file the function catches the FileNotFoundError and
        outputs a short error message before proceeding to the next filename.

        If the specified filename corresponds to a directory the function catches the
        IsADirectoryError and outputs a short error message before proceeding to the next filename.

        If there are more than one filename (TODO: this neglects whether or not these are actual
        files) output the total amount of lines, words and characters.
        """
        valid_files = (True if len(self.filename) > 1 else False)
        for fn in self.filename:
            try:
                with open(fn, 'r') as f: # Using with for automagic closing of files
                    self._count_bytes(f)
                    print ("%8d%8d%8d %s" % (self.line_counter[-1], self.word_counter[-1], self.char_counter[-1], fn))

            except FileNotFoundError:
                print ("wc.py: %s: No such file" % fn)

            except IsADirectoryError:
                print ("wc.py: %s: Is a directory" % fn)

        if valid_files:
            print ("%8d%8d%8d %s" % (sum(self.line_counter), sum(self.word_counter), sum(self.char_counter), "total"))

    def _count_bytes(self, f):
        """Private function for class Word Count calculating the number of lines, words and chars

        The function starts by appending a 0 to the end of the lists line_counter, word_counter
        and char_counter. It then proceeds to iterate through each line in file f. Every time the
        loop repeats the last element in line_counter is incremented by 1, the last element of
        char_counter is incremented by the length of the line, i.e., the number of characters in the
        string line, and the last element of word_counter is incremeneted by the length of the list
        line.split(), i.e., the number of whitespace separated substrings.

        Args:
            f: A file instance.
        """
        self.line_counter.append(0)
        self.word_counter.append(0)
        self.char_counter.append(0)
        for line in f:
            self.line_counter[-1] += 1
            self.char_counter[-1] += len(line)
            self.word_counter[-1] += len(line.split())


if __name__ == '__main__':
    filename = argv[1:]
    if filename[0] == "--usage":
        print (WordCount.__doc__)
        print (WordCount.__init__.__doc__)
        print (WordCount.__call__.__doc__)
        print (WordCount._count_bytes.__doc__)
    else:
        wc = WordCount(filename)
        wc()
