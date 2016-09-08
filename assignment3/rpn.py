from numpy import sqrt, sin, cos

class RPNCalculator:

    def __init__(self):
        self.stack = []
        self.quit = False

    def __call__(self):

        while not self.quit:
            user_input = input(">")
            for i in user_input.split():
                try:
                    temp = float(i)
                    self.stack.append(temp)
                except ValueError:
                    self._execute(i)

    def _execute(self, command):
        if command == '+':
            self.stack.append(self.stack.pop() + self.stack.pop())
        elif command == '*':
            self.stack.append(self.stack.pop() * self.stack.pop())
        elif command == '/':
            self.stack.append(self.stack.pop() / float(self.stack.pop()))
        elif command == 'v':
            self.stack.append(sqrt(self.stack.pop()))
        elif command == 'sin':
            self.stack.append(sin(self.stack.pop()))
        elif command == 'cos':
            self.stack.append(cos(self.stack.pop()))
        elif command == 'p':
            print (self.stack[-1])
        elif command == 'q':
            self.quit = True

if __name__ == '__main__':
    rpn = RPNCalculator()
    rpn()
