import time
from TuringMachine import TuringMachine


class Power(TuringMachine):
    def user_input(self):
        num1 = int(input("Input base number: "))
        num2 = int(input("Input exponent number: "))
        if num1 < 0 or num2 < 0:
            print("Masukkan bilangan positif")
            return self.user_input()
        self.input_string = ""
        for i in range(abs(num1)):
            self.input_string += "0"
        self.input_string += "c"
        for i in range(abs(num2)):
            self.input_string += "0"
        self.input_string += "c"
        return self.input_string


def start_machine():
    tm = Power(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13',
                       'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'H'},
               symbols={'0', '1', 'c', 'B', 'Y', 'X'},
               blank_symbol='B',
               input_symbols={'1', '0', 'c'},
               initial_state='q0',
               accepting_states={'H'},
               transitions={
                   ('q0', '0'): ('q0', '0', 1),
                   ('q0', 'c'): ('q1', 'c', 1),
                   ('q1', '0'): ('q2', 'Y', -1),
                   ('q2', '0'): ('q2', '0', -1),
                   ('q2', 'Y'): ('q2', 'Y', -1),
                   ('q2', 'c'): ('q2', 'c', -1),
                   ('q2', 'B'): ('q3', 'B', 1),
                   ('q3', '0'): ('q4', '0', 1),
                   ('q4', '0'): ('q5', 'X', 1),
                   ('q4', 'c'): ('q7', 'c', -1),
                   ('q5', '0'): ('q5', '0', 1),
                   ('q5', 'Y'): ('q5', 'Y', 1),
                   ('q5', 'c'): ('q5', 'c', 1),
                   ('q5', 'B'): ('q6', '0', -1),
                   ('q6', '0'): ('q6', '0', -1),
                   ('q6', 'Y'): ('q6', 'Y', -1),
                   ('q6', 'c'): ('q6', 'c', -1),
                   ('q6', 'X'): ('q4', 'X', 1),
                   ('q7', 'X'): ('q7', '0', -1),
                   ('q7', '0'): ('q8', '0', 1),
                   ('q8', '0'): ('q8', '0', 1),
                   ('q8', 'c'): ('q10', 'c', 1),
                   ('q9', 'X'): ('q9', '0', -1),
                   ('q9', '0'): ('q8', '0', -1),
                   ('q10', 'Y'): ('q10', 'Y', 1),
                   ('q10', '0'): ('q11', 'Y', -1),
                   ('q10', 'c'): ('q18', 'c', 1),
                   ('q11', '0'): ('q11', '0', -1),
                   ('q11', 'Y'): ('q11', 'Y', -1),
                   ('q11', 'c'): ('q11', 'c', -1),
                   ('q11', 'B'): ('q12', 'B', 1),
                   ('q12', '0'): ('q13', 'X', 1),
                   ('q12', 'c'): ('q9', 'c', -1),
                   ('q13', '0'): ('q13', '0', 1),
                   ('q13', 'Y'): ('q13', 'Y', 1),
                   ('q13', 'c'): ('q13', 'c', 1),
                   ('q13', 'X'): ('q13', 'X', 1),
                   ('q13', 'B'): ('q14', 'B', -1),
                   ('q14', 'X'): ('q14', 'X', -1),
                   ('q14', '0'): ('q15', 'X', -1),
                   ('q14', 'c'): ('q16', 'c', 1),
                   ('q15', '0'): ('q15', '0', -1),
                   ('q15', 'Y'): ('q15', 'Y', -1),
                   ('q15', 'c'): ('q15', 'c', -1),
                   ('q15', 'X'): ('q15', 'X', -1),
                   ('q15', 'B'): ('q13', '0', 1),
                   ('q16', 'X'): ('q16', '0', 1),
                   ('q16', 'B'): ('q17', 'B', -1),
                   ('q17', '0'): ('q17', '0', -1),
                   ('q17', 'Y'): ('q17', 'Y', -1),
                   ('q17', 'c'): ('q17', 'c', -1),
                   ('q17', 'X'): ('q12', 'X', 1),
                   ('q18', '0'): ('q18', 'B', 1),
                   ('q18', 'B'): ('q19', 'B', -1),
                   ('q19', 'B'): ('q19', 'B', -1),
                   ('q19', 'c'): ('q20', 'B', -1),
                   ('q20', 'Y'): ('q20', 'B', -1),
                   ('q20', 'c'): ('H', 'B', -1),
               })

    tm.initialize(dict(enumerate(tm.user_input())))

    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(1)

    tm.print_result()
