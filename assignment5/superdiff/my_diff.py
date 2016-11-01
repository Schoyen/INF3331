

class Superdiff:

    def __init__(self, original_file, modified_file, output_file=None):
        self.original_file = original_file
        self.modified_file = modified_file
        self.output_file = output_file

    def __call__(self):
        original = self._read_from_file(original_file)
        modified = self._read_from_file(modified_file)

    def _read_from_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()
