import time
from TuringMachine import TuringMachine


class Subtraction(TuringMachine):
    def user_input(self):
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        self.input_string = ""
        if num1 < 0 and num2 < 0:
            for i in range(abs(num1)):
                self.input_string += "1"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "1"
            return self.input_string
        elif num1 < 0:
            for i in range(abs(num1)):
                self.input_string += "1"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "0"
            return self.input_string
        elif num2 < 0:
            for i in range(abs(num1)):
                self.input_string += "0"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "1"
            return self.input_string
        else:
            for i in range(abs(num1)):
                self.input_string += "0"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "0"
            return self.input_string


def start_machine():
    tm = Subtraction(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'H'},
                     symbols={'0', '1', 'c', 'B', 'Y'},
                     blank_symbol='B',
                     input_symbols={'1', '0', 'c'},
                     initial_state='q0',
                     accepting_states={'H'},
                     transitions={
                         ('q0', '0'): ('q1', 'B', 1),
                         ('q0', '1'): ('q5', 'B', 1),
                         ('q0', 'c'): ('q9', 'B', 1),
                         ('q1', '0'): ('q1', '0', 1),
                         ('q1', 'c'): ('q2', 'c', 1),
                         ('q2', '1'): ('q2', '1', 1),
                         ('q2', 'Y'): ('q2', 'Y', 1),
                         ('q2', 'B'): ('q3', '1', -1),
                         ('q2', '0'): ('q4', 'Y', -1),
                         ('q3', 'Y'): ('q3', 'Y', -1),
                         ('q3', 'c'): ('q3', 'c', -1),
                         ('q3', '0'): ('q3', '0', -1),
                         ('q3', '1'): ('q3', '1', -1),
                         ('q3', 'B'): ('q0', 'B', 1),
                         ('q4', 'Y'): ('q4', 'Y', -1),
                         ('q4', 'c'): ('q4', 'c', -1),
                         ('q4', '0'): ('q4', '0', -1),
                         ('q4', 'B'): ('q0', 'B', 1),
                         ('q5', '1'): ('q5', '1', 1),
                         ('q5', 'c'): ('q6', 'c', 1),
                         ('q6', '0'): ('q6', '0', 1),
                         ('q6', 'Y'): ('q6', 'Y', 1),
                         ('q6', '1'): ('q8', 'Y', -1),
                         ('q6', 'B'): ('q7', '0', -1),
                         ('q7', 'Y'): ('q7', 'Y', -1),
                         ('q7', '0'): ('q7', '0', -1),
                         ('q7', '1'): ('q7', '1', -1),
                         ('q7', 'c'): ('q7', 'c', -1),
                         ('q7', 'B'): ('q0', 'B', 1),
                         ('q8', 'Y'): ('q8', 'Y', -1),
                         ('q8', '1'): ('q8', '1', -1),
                         ('q8', 'c'): ('q8', 'c', -1),
                         ('q8', 'B'): ('q0', 'B', 1),
                         ('q9', 'Y'): ('q9', 'B', 1),
                         ('q9', '0'): ('q9', '1', 1),
                         ('q9', '1'): ('q9', '0', 1),
                         ('q9', 'B'): ('H', 'B', 1),
                     })

    tm.initialize(dict(enumerate(tm.user_input())))

    while not tm.halted:
        tm.print()
        tm.step()

    tm.print_result()
