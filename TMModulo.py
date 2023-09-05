import time
from TuringMachine import TuringMachine


class Modulo(TuringMachine):
    def user_input(self):
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
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
    tm = Modulo(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'H'},
                symbols={'0', 'c', 'B', 'Y', 'X'},
                blank_symbol='B',
                input_symbols={'0', 'c'},
                initial_state='q0',
                accepting_states={'H'},
                transitions={
                    ('q0', '0'): ('q0', '0', 1),
                    ('q0', 'c'): ('q0', 'c', 1),
                    ('q0', 'B'): ('q1', 'B', -1),
                    ('q1', 'c'): ('q2', 'c', -1),
                    ('q2', '0'): ('q3', 'Y', -1),
                    ('q2', 'c'): ('q7', 'c', 1),
                    ('q3', '0'): ('q3', '0', -1),
                    ('q3', 'c'): ('q4', 'c', -1),
                    ('q4', 'X'): ('q4', 'X', -1),
                    ('q4', 'c'): ('q4', 'c', -1),
                    ('q4', 'B'): ('q10', 'B', 1),
                    ('q4', '0'): ('q5', 'X', 1),
                    ('q5', '0'): ('q5', '0', 1),
                    ('q5', 'X'): ('q5', 'X', 1),
                    ('q5', 'c'): ('q6', 'c', 1),
                    ('q6', '0'): ('q6', '0', 1),
                    ('q6', 'c'): ('q6', 'c', 1),
                    ('q6', 'Y'): ('q2', 'Y', -1),
                    ('q7', 'Y'): ('q7', '0', 1),
                    ('q7', 'c'): ('q8', 'c', -1),
                    ('q8', '0'): ('q8', '0', -1),
                    ('q8', 'c'): ('q8', 'c', -1),
                    ('q8', 'X'): ('q9', 'c', -1),
                    ('q9', 'X'): ('q9', 'c', -1),
                    ('q9', '0'): ('q9', '0', -1),
                    ('q9', 'B'): ('q0', 'B', 1),
                    ('q10', 'X'): ('q11', '0', 1),
                    ('q11', 'c'): ('q11', 'B', 1),
                    ('q11', 'Y'): ('q11', 'B', 1),
                    ('q11', '0'): ('q11', 'B', 1),
                    ('q11', 'X'): ('q11', '0', 1),
                    ('q11', 'B'): ('H', 'B', 1),
                })

    tm.initialize(dict(enumerate(tm.user_input())))

    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(1)

    tm.print_result()
