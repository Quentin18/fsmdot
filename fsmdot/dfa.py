"""
This module implements deterministic finite automatons (DFA).

See: https://en.wikipedia.org/wiki/Deterministic_finite_automaton

Author: Quentin Deschamps
Date: 2020
"""
from collections.abc import Iterable
import pygraphviz as pgv

from fsmdot.fsm import Fsm
from fsmdot.error import FsmError


class Dfa(Fsm):
    """
    Represents a deterministic finite automaton (DFA).

    - Q is a list of states
    - S is the input alphabet (a list of symbols)
    - T is the state-transition table
    - q0 is the initial state, an element of Q
    - F is the set of accept states

    The order of states and symbols is important in Q and S
    to make the state-transition table.

    See: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
    """
    def __init__(self, Q, S, T, q0, F):
        for i in T:
            for s in i:
                if isinstance(s, Iterable) and not isinstance(s, str):
                    raise FsmError(
                        'The state-transition table is not deterministic'
                    )
        super().__init__(Q, S, T, q0, F)

    def accept(self, string):
        """Returns True if the string is accepted by the DFA."""
        state = self._initial_state
        for symbol in string:
            state = self.delta(state, symbol)
            if state is None:
                return False
        return state in self._final_states

    def dot_graph(self):
        """
        Returns the dot graph representing the DFA.

        It uses the pygraphviz library. The method returns an AGraph.
        You can use the write method to write the dot graph to a file.

        See: https://pygraphviz.github.io/
        """
        # Init graph
        G = pgv.AGraph(
            name='DFA', strict=True, directed=True
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
            for v, symbol in zip(line, self._symbols):
                if v is not None:
                    if G.has_edge(u, v):
                        edge = G.get_edge(u, v)
                        edge.attr['label'] += ', ' + str(symbol)
                    else:
                        G.add_edge(u, v, label=str(symbol))

        return G

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
