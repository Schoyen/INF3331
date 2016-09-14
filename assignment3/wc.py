from sys import argv

class WordCount:

    def __init__(self, filename):
        self.filename = filename
        self.line_counter = []
        self.word_counter = []
        self.char_counter = []

    def __call__(self):
        valid_files = (True if len(self.filename) > 1 else False)
        for fn in self.filename:
            try:
                with open(fn, 'r') as f:
                    self._count_bytes(f)
                    print ("%8d%8d%8d %s" % (self.line_counter[-1], self.word_counter[-1], self.char_counter[-1], fn))

            except FileNotFoundError:
                print ("wc.py: %s: No such file or directory" % fn)

        if valid_files:
            print ("%8d%8d%8d %s" % (sum(self.line_counter), sum(self.word_counter), sum(self.char_counter), "total"))

    def _count_bytes(self, f):
        self.line_counter.append(0)
        self.word_counter.append(0)
        self.char_counter.append(0)
        for line in f:
            self.line_counter[-1] += 1
            self.char_counter[-1] += len(line)
            self.word_counter[-1] += len(line.split())


if __name__ == '__main__':
    filename = argv[1:]
    wc = WordCount(filename)
    wc()
