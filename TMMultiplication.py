import time
from TuringMachine import TuringMachine


class Multiplication(TuringMachine):
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
            self.input_string += "c"
            return self.input_string
        elif num1 < 0:
            for i in range(abs(num1)):
                self.input_string += "1"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "0"
            self.input_string += "c"
            return self.input_string
        elif num2 < 0:
            for i in range(abs(num1)):
                self.input_string += "0"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "1"
            self.input_string += "c"
            return self.input_string
        else:
            for i in range(abs(num1)):
                self.input_string += "0"
            self.input_string += "c"
            for i in range(abs(num2)):
                self.input_string += "0"
            self.input_string += "c"
            return self.input_string


def start_machine():
    tm = Multiplication(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7',
                                'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17',
                                'q18', 'q19', 'H'},
                        symbols={'0', '1', 'c', 'B', 'X', 'Y'},
                        blank_symbol='B',
                        input_symbols={'1', '0', 'c'},
                        initial_state='q0',
                        accepting_states={'H'},
                        transitions={
                            ('q0', '0'): ('q1', 'B', 1),
                            ('q0', '1'): ('q9', 'B', 1),
                            ('q0', 'c'): ('q19', 'B', 1),
                            ('q1', '0'): ('q1', '0', 1),
                            ('q1', 'c'): ('q2', 'c', 1),
                            ('q2', '0'): ('q3', 'X', 1),
                            ('q2', 'c'): ('q17', 'c', -1),
                            ('q2', '1'): ('q6', 'Y', 1),
                            ('q3', '0'): ('q3', '0', 1),
                            ('q3', 'c'): ('q4', 'c', 1),
                            ('q4', '0'): ('q4', '0', 1),
                            ('q4', 'B'): ('q5', '0', -1),
                            ('q5', '0'): ('q5', '0', -1),
                            ('q5', 'c'): ('q5', 'c', -1),
                            ('q5', 'X'): ('q2', 'X', 1),
                            ('q6', 'c'): ('q7', 'c', 1),
                            ('q6', '1'): ('q6', '1', 1),
                            ('q7', '1'): ('q7', '1', 1),
                            ('q7', 'B'): ('q8', '1', -1),
                            ('q8', '1'): ('q8', '1', -1),
                            ('q8', 'c'): ('q8', 'c', -1),
                            ('q8', 'Y'): ('q2', 'Y', 1),
                            ('q9', '1'): ('q9', '1', 1),
                            ('q9', 'c'): ('q10', 'c', 1),
                            ('q10', '0'): ('q11', 'X', 1),
                            ('q10', '1'): ('q14', 'Y', 1),
                            ('q10', 'c'): ('q17', 'c', -1),
                            ('q11', '0'): ('q11', '0', 1),
                            ('q11', 'c'): ('q12', 'c', 1),
                            ('q12', '1'): ('q12', '1', 1),
                            ('q12', 'B'): ('q13', '1', -1),
                            ('q13', '0'): ('q13', '0', -1),
                            ('q13', '1'): ('q13', '1', -1),
                            ('q13', 'c'): ('q13', 'c', -1),
                            ('q13', 'X'): ('q10', 'X', 1),
                            ('q14', '1'): ('q14', '1', 1),
                            ('q14', 'c'): ('q15', 'c', 1),
                            ('q15', '0'): ('q15', '0', 1),
                            ('q15', 'B'): ('q16', '0', -1),
                            ('q16', '0'): ('q16', '0', -1),
                            ('q16', '1'): ('q16', '1', -1),
                            ('q16', 'c'): ('q16', 'c', -1),
                            ('q16', 'Y'): ('q10', 'Y', 1),
                            ('q17', 'c'): ('q18', 'c', -1),
                            ('q17', 'X'): ('q17', '0', -1),
                            ('q17', 'Y'): ('q17', '1', -1),
                            ('q18', '0'): ('q18', '0', -1),
                            ('q18', '1'): ('q18', '1', -1),
                            ('q18', 'B'): ('q0', 'B', 1),
                            ('q19', '0'): ('q19', 'B', 1),
                            ('q19', '1'): ('q19', 'B', 1),
                            ('q19', 'c'): ('H', 'B', 1),
                        })

    tm.initialize(dict(enumerate(tm.user_input())))

    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(1)

    tm.print_result()
