

class Superdiff:

    def __init__(self, original_file, modified_file, output_file=None):
        self.original_file = original_file
        self.modified_file = modified_file
        self.output_file = output_file

    def __call__(self):
        original = self._read_from_file(original_file)
        modified = self._read_from_file(modified_file)
        for i in range(len(original)):
            if i < len(modified):
                if original[i] == modified[i]:
                    print ("0 %s" % original[i])

    def _read_from_file(self, filename):
        with open(filename, 'r') as f:
            return [line for line in f]

if __name__ == '__main__':
    from sys import argv
    try:
        original_file = argv[1]
        modified_file = argv[2]
    except IndexError:
        raise IndexError("Usage: %s <original file> <modified file> <output file> (optional)" % argv[0])

    try:
        sd = Superdiff(original_file, modified_file, argv[3])
    except IndexError:
        sd = Superdiff(original_file, modified_file)

    sd()
