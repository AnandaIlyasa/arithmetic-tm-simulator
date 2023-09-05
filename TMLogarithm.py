import time
from TuringMachine import TuringMachine


class Logarithm(TuringMachine):
    def user_input(self):
        num1 = int(input("Input number: "))
        if num1 < 0:
            print("Masukkan bilangan positif")
            return self.user_input()
        self.input_string = ""
        for i in range(abs(num1)):
            self.input_string += "0"
        return self.input_string


def start_machine():
    tm = Logarithm(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7',
                           'q8', 'q9', 'q10', 'q11', 'H'},
                   symbols={'0', '1', 'X', 'B'},
                   blank_symbol='B',
                   input_symbols={'0'},
                   initial_state='q0',
                   accepting_states={'H'},
                   transitions={
                       ('q0', '0'): ('q1', '0', 1),
                       ('q0', 'B'): ('H', 'B', 1),
                       ('q1', '0'): ('q2', '0', 1),
                       ('q1', 'B'): ('q11', 'B', -1),
                       ('q2', '0'): ('q3', 'X', 1),
                       ('q2', 'B'): ('q11', 'B', -1),
                       ('q3', '0'): ('q4', 'X', -1),
                       ('q3', 'X'): ('q3', 'X', 1),
                       ('q3', 'B'): ('q7', 'B', -1),
                       ('q4', '1'): ('q4', '1', -1),
                       ('q4', '0'): ('q4', '0', -1),
                       ('q4', 'X'): ('q4', 'X', -1),
                       ('q4', 'B'): ('q5', 'B', 1),
                       ('q5', '1'): ('q6', '0', 1),
                       ('q5', '0'): ('q5', '1', 1),
                       ('q5', 'X'): ('q6', '0', 1),
                       ('q6', '1'): ('q6', '1', 1),
                       ('q6', '0'): ('q6', '0', 1),
                       ('q6', 'X'): ('q3', 'X', 1),
                       ('q7', '1'): ('q7', '1', -1),
                       ('q7', '0'): ('q7', '0', -1),
                       ('q7', 'X'): ('q7', 'B', -1),
                       ('q7', 'B'): ('q8', 'B', 1),
                       ('q8', '1'): ('q8', '0', 1),
                       ('q8', '0'): ('q9', '0', 1),
                       ('q9', '1'): ('q9', '0', 1),
                       ('q9', '0'): ('q10', '0', 1),
                       ('q9', 'B'): ('q11', 'B', -1),
                       ('q10', '1'): ('q10', '0', 1),
                       ('q10', '0'): ('q10', '0', 1),
                       ('q10', 'B'): ('H', 'B', -1),
                       ('q11', '0'): ('H', 'B', -1),
                   })

    tm.initialize(dict(enumerate(tm.user_input())))

    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(1)

    tm.print_result()
