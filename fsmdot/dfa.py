"""
This module implements deterministic finite automatons (DFA).

See: https://en.wikipedia.org/wiki/Deterministic_finite_automaton

Author: Quentin Deschamps
Date: 2020
"""
from collections.abc import Iterable

from fsmdot.fsm import Fsm
from fsmdot.error import FsmError


class Dfa(Fsm):
    """
    Represents a deterministic finite automaton (DFA).

    - Q is a set of states
    - S is a set of input symbols (alphabet)
    - d is a dictionnary containing the transitions
    - q0 is the initial state
    - F is the set of accept states

    See: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
    """
    def __init__(self, Q, S, d, q0, F):
        super().__init__(Q, S, d, q0, F, True)

    def accept(self, string):
        """Returns True if the string is accepted by the DFA."""
        state = self._initial_state
        for symbol in string:
            state = self.delta(state, symbol)
            if state is None:
                return False
        return state in self._final_states

    def unreachable_states(self):
        """
        Returns the set of unreachable states of the DFA.

        See: https://en.wikipedia.org/wiki/DFA_minimization#Unreachable_states
        """
        reachable_states = {self._initial_state}
        new_states = {self._initial_state}
        while new_states:
            temp = set()
            for state in new_states:
                for symbol in self._symbols:
                    temp.add(self.delta(state, symbol))
            new_states = temp.difference(reachable_states)
            reachable_states.update(new_states)
        return set(self._states).difference(reachable_states)

    def minimize(self):
        """
        Transforms a DFA into an equivalent DFA that has a minimum number
        of states.

        See:
        https://en.wikipedia.org/wiki/DFA_minimization
        """
        pass
