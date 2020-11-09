"""
This module implements nondeterministic finite automatons (NFA).

See: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton

Author: Quentin Deschamps
Date: 2020
"""
import pygraphviz as pgv

from fsmdot.fsm import fsm
from fsmdot.dfa import dfa


class nfa(fsm):
    """
    Represents a nondeterministic finite automaton (NFA).

    - Q is a list of states
    - S is the input alphabet (a list of symbols)
    - T is the state-transition table
    - q0 is the initial state, an element of Q
    - F is the set of accept states

    The order of states and symbols is important in Q and S
    to make the state-transition table.

    You can add epsilon-moves using the nfa.EPSILON character in S.

    See: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
    """
    EPSILON = chr(949)

    def has_epsilon_moves(self):
        """Returns True if the NFA has epsilon-moves."""
        return nfa.EPSILON in self._symbols

    def accept(self, string):
        """Returns True if the string is accepted by the NFA."""
        epsilon_nfa = self.has_epsilon_moves()
        if epsilon_nfa:
            current_states = self.epsilon_closure(self._initial_state)
        else:
            current_states = {self._initial_state}
        for symbol in string:
            new_states = set()
            for state in current_states:
                t = self.delta(state, symbol)
                if epsilon_nfa:
                    for s in t:
                        new_states.update(self.epsilon_closure(s))
                else:
                    new_states.update(t)
            current_states = new_states
        return bool(current_states.intersection(self._final_states))

    def epsilon_closure(self, state):
        """Returns the epsilon closure of a state."""
        c = {state}
        self._recursive_closure(state, c)
        return c

    def _recursive_closure(self, state, c):
        c.add(state)
        for s in self.delta(state, nfa.EPSILON):
            self._recursive_closure(s, c)

    def to_dfa(self):
        """Returns the DFA corresponding to the NFA."""
        symbols = self._symbols.copy()
        symbols.remove(nfa.EPSILON)
        states = []
        table = []
        final_states = set()
        new_states = [self.epsilon_closure(self._initial_state)]
        initial_state = str(new_states[0])
        while new_states:
            state = new_states.pop()
            states.append(str(state))
            if self._final_states.intersection(state):
                final_states.add(str(state))
            line = []
            for symbol in symbols:
                t = set()
                for s in state:
                    for i in self.delta(s, symbol):
                        t.update(self.epsilon_closure(i))
                if t:
                    line.append(str(t))
                    if str(t) not in states and t not in new_states:
                        new_states.append(t)
                else:
                    line.append(None)
            table.append(line)

        return dfa(states, symbols, table, initial_state, final_states)

    def dot_graph(self):
        """
        Returns the dot graph representing the NFA.

        It uses the pygraphviz library. The method returns an AGraph.
        You can use the write method to write the dot graph to a file.

        See: https://pygraphviz.github.io/
        """
        # Init graph
        G = pgv.AGraph(
            name='NFA', strict=True, directed=True
        )
        G.graph_attr['rankdir'] = 'LR'
        G.node_attr['shape'] = 'circle'

        # Init nodes
        G.add_nodes_from(self._states)

        # Initial state
        G.add_node('null', shape='point')
        G.add_edge('null', self._initial_state)

        # Final states
        G.add_nodes_from(self._final_states, shape='doublecircle')

        # Transitions
        for line, u in zip(self._table, self._states):
            for states, symbol in zip(line, self._symbols):
                for v in states:
                    if G.has_edge(u, v):
                        edge = G.get_edge(u, v)
                        edge.attr['label'] += ', ' + symbol
                    else:
                        G.add_edge(u, v, label=symbol)

        return G
