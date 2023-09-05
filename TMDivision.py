import time
from TuringMachine import TuringMachine


class Division(TuringMachine):
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
    tm = Division(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7',
                          'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17',
                          'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'H'},
                  symbols={'0', '1', 'c', 'B', 'X', 'Y'},
                  blank_symbol='B',
                  input_symbols={'1', '0', 'c'},
                  initial_state='q0',
                  accepting_states={'H'},
                  transitions={
                      ('q0', '0'): ('q1', '0', 1),
                      ('q0', '1'): ('q7', '1', 1),
                      ('q1', '0'): ('q1', '0', 1),
                      ('q1', 'c'): ('q2', 'c', 1),
                      ('q2', '0'): ('q2', '0', 1),
                      ('q2', '1'): ('q2', '1', 1),
                      ('q2', 'c'): ('q3', 'c', -1),
                      ('q3', '0'): ('q4', 'X', -1),
                      ('q3', '1'): ('q4', 'Y', -1),
                      ('q3', 'c'): ('q13', 'c', 1),
                      ('q3', 'X'): ('q3', 'X', -1),
                      ('q3', 'Y'): ('q3', 'Y', -1),
                      ('q4', '0'): ('q4', '0', -1),
                      ('q4', '1'): ('q4', '1', -1),
                      ('q4', 'c'): ('q4', 'c', -1),
                      ('q4', 'B'): ('q5', 'B', 1),
                      ('q5', '0'): ('q6', 'B', 1),
                      ('q5', 'c'): ('q23', 'B', 1),
                      ('q6', '0'): ('q6', '0', 1),
                      ('q6', '1'): ('q6', '1', 1),
                      ('q6', 'c'): ('q6', 'c', 1),
                      ('q6', 'X'): ('q3', 'X', -1),
                      ('q6', 'Y'): ('q3', 'Y', -1),
                      ('q7', '1'): ('q7', '1', 1),
                      ('q7', 'c'): ('q8', 'c', 1),
                      ('q7', 'B'): ('q8', 'B', -1),
                      ('q8', '0'): ('q8', '0', 1),
                      ('q8', '1'): ('q8', '1', 1),
                      ('q8', 'c'): ('q9', 'c', -1),
                      ('q9', '0'): ('q10', 'X', -1),
                      ('q9', '1'): ('q10', 'Y', -1),
                      ('q9', 'c'): ('q18', 'c', 1),
                      ('q9', 'X'): ('q9', 'X', -1),
                      ('q9', 'Y'): ('q9', 'Y', -1),
                      ('q10', '0'): ('q10', '0', -1),
                      ('q10', '1'): ('q10', '1', -1),
                      ('q10', 'c'): ('q10', 'c', -1),
                      ('q10', 'B'): ('q11', 'B', 1),
                      ('q11', '1'): ('q12', 'B', 1),
                      ('q11', 'c'): ('q23', 'B', 1),
                      ('q12', '1'): ('q12', '1', 1),
                      ('q12', 'c'): ('q12', 'c', 1),
                      ('q12', 'X'): ('q9', 'X', -1),
                      ('q12', '0'): ('q12', '0', 1),
                      ('q12', 'Y'): ('q9', 'Y', -1),
                      ('q13', 'X'): ('q16', '0', 1),
                      ('q13', 'Y'): ('q14', '1', 1),
                      ('q14', '1'): ('q14', '1', 1),
                      ('q14', 'c'): ('q14', 'c', 1),
                      ('q14', 'Y'): ('q14', '1', 1),
                      ('q14', 'B'): ('q15', '1', -1),
                      ('q15', '1'): ('q15', '1', -1),
                      ('q15', 'c'): ('q3', 'c', -1),
                      ('q16', '0'): ('q16', '0', 1),
                      ('q16', 'c'): ('q16', 'c', 1),
                      ('q16', 'X'): ('q16', '0', 1),
                      ('q16', 'B'): ('q17', '0', -1),
                      ('q17', '0'): ('q17', '0', -1),
                      ('q17', 'c'): ('q3', 'c', -1),
                      ('q18', 'X'): ('q21', '0', 1),
                      ('q18', 'Y'): ('q19', '1', 1),
                      ('q19', '0'): ('q19', '0', 1),
                      ('q19', 'c'): ('q19', 'c', 1),
                      ('q19', 'Y'): ('q19', '1', 1),
                      ('q19', 'B'): ('q20', '0', -1),
                      ('q20', '0'): ('q20', '0', -1),
                      ('q20', 'c'): ('q9', 'c', -1),
                      ('q21', '1'): ('q21', '1', 1),
                      ('q21', 'c'): ('q21', 'c', 1),
                      ('q21', 'X'): ('q21', '0', 1),
                      ('q21', 'B'): ('q22', '1', -1),
                      ('q22', '1'): ('q22', '1', -1),
                      ('q22', 'c'): ('q9', 'c', -1),
                      ('q23', '0'): ('q23', 'B', 1),
                      ('q23', '1'): ('q23', 'B', 1),
                      ('q23', 'c'): ('H', 'B', 1),
                      ('q23', 'X'): ('q23', 'B', 1),
                      ('q23', 'Y'): ('q23', 'B', 1),
                  })

    tm.initialize(dict(enumerate(tm.user_input())))

    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(1)

    tm.print_result()
