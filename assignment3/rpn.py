from numpy import sqrt, sin, cos, pi # Allow complex values
from sys import argv # Read input from command line

class RPNCalculator:
    """RPNCalculator is a Reverse Polish Notation calculator.

    The RPNCalculator is a calculator that can be run with command
    line arguments and/or from prompt.

    Attributes:
        stack: A list treated as a stack. Used for appending and
            popping of values recieved from used.
        quit: A boolean value used to determine if the user wishes
            to exit the program.
        command_line: A list of optional additional command line arguments.
    """
    def __init__(self, command_line = None):
        """Constructor for class RPNCalculator.

        Args:
            command_line: An optional list of additional command line arguments.
        """

        self.stack = [] # Internal stack
        self.quit = False # Boolean value to determine if 'q' is input (i.e., quit)
        self.command_line = command_line or [] # Optional command line input

    def __call__(self):
        """Calling function for class RPNCalculator

        The __call__ function first processes the command line input if there are any.
        It then proceeds to run the user prompt querying the user for input. When input
        has been the recieved it is split into a whitespace-separated list and sent to
        the private function _process_input.

        The user prompt is run until a 'q' has been recieved from the user, thus setting
        the boolean value quit = True.
        """

        self._process_input(self.command_line) # Process command line input first

        while not self.quit: # Loop until a 'q' has been input
            user_input = input("> ") # Output "> " and wait for user input
            self._process_input(user_input.split()) # Process input from user


    def _process_input(self, user_input):
        """Private function for class RPNCalculator processing user input.

        The function runs through all elements in the iterable list user_input
        and attempts to convert each element into a float. If the current element
        is a float it is appended to the end of the stack, i.e., the list stack.
        If a ValueError is raised, the function sends the input to the private
        function _execute as a potential command.

        Args:
            user_input: A list of argument strings.
        """

        for i in user_input: # Iterate over user_input
            try: # Hacky-solution to string-number conversion
                temp = float(i) # Check if 'i' can be a float
                self.stack.append(temp) # Append 'i' to the end of the stack
            except ValueError: # If float(i) didn't work, treat 'i' as a command
                self._execute(i) # Execute command with _execute

    def _execute(self, command):
        """Private function for class RPNCalculator executing commands.

        The function runs through a series of conditionals in order
        to determine which command has been requested by the user.

        Args:
            command: A string.
        """
        if command == 'q': # Check if the user wishes to quit the program
            self.quit = True
            return

        if command == 'pi': # Check if the user wants to insert pi
            self.stack.append(pi)
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
        """Private function for class RPNCalculator testing if a string can be a complex number.

        The function tries to convert all but the last character (i.e., 'j' or 'J') in c_number
        as a float.

        Args:
            c_number: A string.
        """

        try: # Check if all but the last character in c_string are numbers
            temp = float(c_number[0:-1])
            self.stack.append(complex(0, temp))
        except ValueError: # If not, do nothing
            pass


if __name__ == '__main__':
    command_line_input = argv[1:] # Get command line input excluding the program name
    if command_line_input and command_line_input[0] == "--usage":
        print (RPNCalculator.__doc__)
        print (RPNCalculator.__init__.__doc__)
        print (RPNCalculator.__call__.__doc__)
        print (RPNCalculator._process_input.__doc__)
        print (RPNCalculator._execute.__doc__)
        print (RPNCalculator._test_complex.__doc__)

    else:
        rpn = RPNCalculator(command_line_input) # Create an instance of RPNCalculator
        rpn() # Call RPNCalculator
