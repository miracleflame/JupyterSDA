class Calculator:
    def __init__(self, initial_value):
        self.current_value = initial_value
        self.results_history = []

    def add(self, x):
        self.results_history.append(self.current_value)
        self.current_value += x

    def divide(self, x):
        if x == 0:
            return False

        self.results_history += [self.current_value]
        self.current_value /= x
        return True

    def subtract(self, x):
        self.results_history += [self.current_value]
        self.current_value -= x

    def multiply(self, x):
        self.results_history += [self.current_value]
        self.current_value = self.current_value * x

    def undo(self):
        if not self.results_history:
            self.current_value = 0
        else:
            self.current_value = self.results_history.pop()

    # self.current_value = self.results_history.pop() if self.results_history else 0