import time
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class TuringMachine:
    states: set[str]
    symbols: set[str]
    blank_symbol: str
    input_symbols: set[str]
    initial_state: str
    accepting_states: set[str]
    transitions: dict[tuple[str, str], tuple[str, str, int]]
    # state, symbol -> new state, new symbol, direction

    head: int = field(init=False)
    tape: defaultdict[int, str] = field(init=False)
    current_state: str = field(init=False)
    halted: bool = field(init=False, default=True)
    input_string: str = field(init=False)

    def initialize(self, input_symbols: dict[int, str]):
        self.head = 0
        self.halted = False
        self.current_state = self.initial_state
        self.tape = defaultdict(lambda: self.blank_symbol, input_symbols)

    def step(self):
        if self.halted:
            raise RuntimeError('Cannot step halted machine')

        try:
            state, symbol, direction = self.transitions[(self.current_state, self.tape[self.head])]
        except KeyError:
            self.halted = True
            return
        self.tape[self.head] = symbol
        self.current_state = state
        self.head += direction

    def print_result(self):
        result = 0
        for k, v in self.tape.items():
            if v == '0':
                result += 1
            elif v == '1':
                result -= 1
        print(f'Result = {result}')

    def print(self, window=10):
        print('    ' + '_' * 85)
        print('... | ', end='')
        print(' | '.join(self.tape[i] for i in range(self.head - window, self.head + window + 1)), end='')
        print(f' | ... state={self.current_state}')
        print('    ' + '-' * 85)
        print(f'{" " * (4 * window + 6)}^')
