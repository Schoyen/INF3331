from numpy import zeros

class Superdiff:
    """Class Superdiff implementing the longest common subsequnce function as a diff-tool.

    Superdiff implements the function found here:
    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#LCS_function_defined

    This class also contains method for reading in text from files, print the diff
    between two files or output the result to file.
    """

    def __init__(self, original_file, modified_file, output_file=None):
        """Constructor for Superdiff.

        Args:
            original_file: The filename of the original file to be compared.
            modified_file: The filename of the modified file to be compared to the original
                           file.
            output_file: The filename of an optional output file.
        """
        self.original_file = original_file
        self.modified_file = modified_file
        self.output_file = output_file
        self.output = [] # An empty list used to store diff-lines

    def __call__(self):
        """Calling function for Superdiff.

        The __call__ function takes care of calling the correct methods in order to read in
        the data, calculate the longest common subsequence and ouputting the result to
        screen or file.
        """
        original = self._read_from_file(original_file)
        modified = self._read_from_file(modified_file)
        subsequence = self._longest_common_subsequence(original, modified)
        self._generate_output(subsequence, original, modified, len(original), len(modified))
        # Check if the result should be written to file or to standard out
        if self.output_file:
            self._write_to_file(self.output_file)
        else:
            self._output_to_screen(self.output)

    def _write_to_file(self, filename):
        """Function used to write the data stored in Superdiff.output to file.

        Args:
            filename: The filename of the output-file.
        """
        with open(filename, 'w') as f:
            for i in self.output:
                f.write("%s\n" % i) # Append a new-line

    def _output_to_screen(self, output):
        """Function used to write the data stored in Superdiff.output to screen.

        Args:
            output: The output to be printed.
        """
        for i in output:
            print(i)

    def _generate_output(self, subsequence, original, modified, i, j):
        """
        Massive inspiration:
        https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Print_the_diff
        """
        if i > 0 and j > 0 and original[i - 1] == modified[j - 1]:
            self._generate_output(subsequence, original, modified, i - 1, j - 1)
            self.output.append("0 %s" % original[i - 1])
        elif j > 0 and (i == 0 or subsequence[i][j - 1] >= subsequence[i - 1][j]):
            self._generate_output(subsequence, original, modified, i, j - 1)
            self.output.append("+ %s" % modified[j - 1])
        elif i > 0 and (j == 0 or subsequence[i][j - 1] < subsequence[i - 1][j]):
            self._generate_output(subsequence, original, modified, i - 1, j)
            self.output.append("- %s" % original[i - 1])

    def _longest_common_subsequence(self, original, modified):
        """
        Massive inspiration:
        https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Computing_the_length_of_the_LCS
        """
        subsequence = zeros((len(original) + 1, len(modified) + 1))
        for i in range(1, len(original) + 1):
            for j in range(1, len(modified) + 1):
                if original[i - 1] == modified[j - 1]:
                    subsequence[i][j] = subsequence[i - 1][j - 1] + 1
                else:
                    subsequence[i][j] = max(subsequence[i][j  - 1], subsequence[i - 1][j])

        return subsequence

    def _read_from_file(self, filename):
        with open(filename, 'r') as f:
            return [line.strip('\n') for line in f]

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
