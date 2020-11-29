"""
This module implements nondeterministic finite automatons (NFA).

See: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton

Author: Quentin Deschamps
Date: 2020
"""
from fsmdot.fsm import Fsm
from fsmdot.dfa import Dfa


class Nfa(Fsm):
    """
    Represents a nondeterministic finite automaton (NFA).

    - Q is a set of states
    - S is a set of input symbols (alphabet)
    - d is a dictionnary containing the transitions
    - q0 is the initial state
    - F is the set of accept states

    You can add epsilon-moves using the Nfa.EPSILON character in S.

    See: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
    """
    EPSILON = chr(949)

    def has_epsilon_moves(self):
        """Returns True if the NFA has epsilon-moves."""
        return Nfa.EPSILON in self._symbols

    def accept(self, string):
        """Returns True if the string is accepted by the NFA."""
        current_states = self.epsilon_closure(self._initial_state)
        for symbol in string:
            new_states = set()
            for state in current_states:
                t = self.delta(state, symbol)
                for s in t:
                    new_states.update(self.epsilon_closure(s))
            current_states = new_states
        return bool(current_states.intersection(self._final_states))

    def epsilon_closure(self, state):
        """Returns the epsilon closure of a state."""
        c = {state}
        if self.has_epsilon_moves():
            self._recursive_closure(state, c)
        return c

    def _recursive_closure(self, state, c):
        c.add(state)
        for s in self.delta(state, Nfa.EPSILON):
            self._recursive_closure(s, c)

    def to_dfa(self):
        """
        Returns the DFA corresponding to the NFA.

        It uses the powerset construction.

        See: https://en.wikipedia.org/wiki/Powerset_construction
        """
        symbols = set(self._symbols)
        if self.has_epsilon_moves():
            symbols.remove(Nfa.EPSILON)
        states = set()
        transitions = dict()
        final_states = set()
        new_states = [self.epsilon_closure(self._initial_state)]
        initial_state = str(new_states[0])
        while new_states:
            state = new_states.pop()
            new_state = str(state)
            states.add(new_state)
            if self._final_states.intersection(state):
                final_states.add(new_state)
            transitions[new_state] = dict()
            for symbol in symbols:
                t = set()
                for s in state:
                    for i in self.delta(s, symbol):
                        t.update(self.epsilon_closure(i))
                if t:
                    transitions[new_state][symbol] = str(t)
                    if str(t) not in states and t not in new_states:
                        new_states.append(t)

        return Dfa(states, symbols, transitions, initial_state, final_states)
