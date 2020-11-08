"""
This module implements finite-state machines.

See: https://en.wikipedia.org/wiki/Finite-state_machine

Author: Quentin Deschamps
Date: 2020
"""
from abc import ABC
from tabulate import tabulate

from fsmdot.error import fsmError


class fsm(ABC):
    """Represents a finite-state machine.

    - Q is a list of states
    - S is the input alphabet (a list of symbols)
    - T is the state-transition table
    - q0 is the initial state, an element of Q
    - F is the set of accept states

    The order of states and symbols is important in Q and S
    to make the state-transition table.

    See: https://en.wikipedia.org/wiki/Finite-state_machine
    """
    def __init__(self, Q, S, T, q0, F):
        if not isinstance(Q, list):
            raise fsmError('Q must be a list')
        if not isinstance(S, list):
            raise fsmError('S must be a list')
        if q0 not in Q:
            raise fsmError('Q does not contain q0')
        F = set(F)
        if F.intersection(Q) != F:
            raise fsmError('Q does not contain all states of F')
        self._states = Q
        self._symbols = S
        self._table = T
        self._initial_state = q0
        self._final_states = F

    @property
    def states(self):
        return self._states

    @property
    def symbols(self):
        return self._symbols

    @property
    def table(self):
        return self._table

    @property
    def initial_state(self):
        return self._initial_state

    @property
    def final_states(self):
        return self._final_states

    def _get_state_index(self, state):
        return self._states.index(state)

    def _get_symbol_index(self, symbol):
        return self._symbols.index(symbol)

    def print_table(self):
        """
        Prints the state-transition table.

        - The initial state is indicated with an arrow: ->
        - The accept states are indicated with a star: *
        """
        states = []
        for s in self._states:
            if s == self._initial_state:
                states.append('-> ' + str(s))
            elif s in self._final_states:
                states.append('* ' + str(s))
            else:
                states.append(str(s))
        print(tabulate(
            self._table,
            headers=self._symbols,
            tablefmt='grid',
            showindex=states,
            stralign='right'
            )
        )

    def delta(self, state, symbol):
        """State-transition function."""
        i = self._get_state_index(state)
        j = self._get_symbol_index(symbol)
        return self._table[i][j]
