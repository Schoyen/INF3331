from cmath import sqrt, sin, cos # Allow complex values
from sys import argv # Read input from command line

class RPNCalculator:
    """Class RPNCalculator is a calculator in Reverse Polish Notation.
    The RPNCalculator can be run with command line arguments and/or from prompt.

    <object-instance> = RPNCalculator(<optional input from command line>) # Initializes program
    <object-instance>() # Calling __call__ to start program.
    """

    def __init__(self, command_line = None):
        """Constructor for RPNCalculator

        Input:
            @param: command_line = None
                    Optional additional input from command line.
                    command_line must be a list.
        """

        self.stack = [] # Internal stack
        self.quit = False # Boolean value to determine if 'q' is input (i.e., quit)
        self.command_line = command_line # Optional command line input

    def __call__(self):
        """Calling function in RPNCalculator

        This function runs the user prompt and calls another function _process_input to
        process input from prompt.
        """

        if type(self.command_line) == list: # Check if self.command_line is a list
            self._process_input(self.command_line) # If self.command_line is a list, process the commands and/or numbers

        while not self.quit: # Loop until a 'q' has been input
            user_input = input("> ") # Output "> " and wait for user input
            self._process_input(user_input.split()) # Process input from user


    def _process_input(self, user_input):
        """Function used to test input from user.

        Input:
            @param: user_input
                    The user_input must be iterable, e.g., a list.
        """

        for i in user_input: # Iterate over user_input
            try: # Hacky-solution to string-number conversion
                temp = float(i) # Check if 'i' can be a float
                self.stack.append(temp) # Append 'i' to the end of the stack
            except ValueError: # If float(i) didn't work, treat 'i' as a command
                self._execute(i) # Execute command with _execute

    def _execute(self, command):
        """Function used to execute commands.

        Input:
            @param: command
                    The command is treated as a string
        """

        if command == 'q': # Check if the user wishes to quit the program
            self.quit = True
            return

        if command[-1] == 'j' or command[-1] == 'J': # Check if command can be a complex number
            self._test_complex(command)


        if len(self.stack) >= 1: # Check if self.stack is long enough to be popped or called with self.stack[-1]
            if command == 'p': # Output last element on the stack
                print (self.stack[-1])
            elif command == 'v': # Take the square root of the last element on stack
                self.stack.append(sqrt(self.stack.pop())) # Append to the end the square root of the popped result
            elif command == 'sin': # Find the sine of the last element on the stack
                self.stack.append(sin(self.stack.pop()))
            elif command == 'cos': # Find the cosine of the last element on the stack
                self.stack.append(cos(self.stack.pop()))

        if len(self.stack) >= 2: # Check if self.stack is long enough to be popped twice, i.e., at least two numbers are on the stack
            if command == '+': # Add the two last elements
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif command == '*': # Multiply the two last elements
                self.stack.append(self.stack.pop() * self.stack.pop())
            elif command == '/': # Divide the two last elements
                self.stack.append(self.stack.pop() / float(self.stack.pop()))

    def _test_complex(self, c_number):
        """Function testing if the input c_number can be treated as a complex number,
        i.e., all characters are numbers except for last which will be 'j' or 'J'.

        Input:
            @param: c_number
                    The input c_number is a string
        """

        try: # Check if all but the last character in c_string are numbers
            temp = float(c_number[0:-1])
            self.stack.append(complex(0, temp))
        except ValueError: # If not, do nothing
            pass


if __name__ == '__main__':
    command_line_input = argv[1:] # Get command line input excluding the program name
    rpn = RPNCalculator(command_line_input) # Create an instance of RPNCalculator
    rpn() # Call RPNCalculator
