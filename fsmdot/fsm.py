"""
This module implements finite-state machines.

See: https://en.wikipedia.org/wiki/Finite-state_machine

Author: Quentin Deschamps
Date: 2020
"""
from abc import ABC
from tabulate import tabulate
import pygraphviz as pgv
from collections.abc import Iterable

from fsmdot.error import FsmError


class Fsm(ABC):
    """Represents a finite-state machine.

    - Q is a set of states
    - S is a set of input symbols (alphabet)
    - d is a dictionnary containing the transitions
    - q0 is the initial state
    - F is the set of accept states

    See: https://en.wikipedia.org/wiki/Finite-state_machine
    """
    def __init__(self, Q, S, d, q0, F, is_deterministic):
        if q0 not in Q:
            raise FsmError('Q does not contain q0')
        F = set(F)
        if F.intersection(Q) != F:
            raise FsmError('Q does not contain all states of F')
        Fsm._valid_transitions(Q, S, d, is_deterministic)
        self._states = set(Q)
        self._symbols = set(S)
        self._transitions = d
        self._initial_state = q0
        self._final_states = F
        self._is_deterministic = is_deterministic

    @staticmethod
    def _valid_transitions(Q, S, d, is_deterministic):
        """Raises an error if the dictionnary of transitions d is not valid"""
        if not isinstance(d, dict):
            raise FsmError('The transitions must be a dictionnay')
        for state in d:
            if state not in Q:
                raise FsmError('%s is not in the set of states' % state)
            if not isinstance(d[state], dict):
                raise FsmError(
                    'You must associate a dictionnary with the key %s' % state
                )
            for symbol in d[state]:
                if symbol not in S:
                    raise FsmError('%s is not in the set of symbols' % symbol)
                t = d[state][symbol]
                is_it = isinstance(t, Iterable) and not isinstance(t, str)
                if is_deterministic:
                    if is_it:
                        raise FsmError(
                            'The dictionnary is not deterministic'
                        )
                    if t not in Q:
                        raise FsmError(
                            '%s is not in the set of states' % t
                        )
                else:
                    if not is_it:
                        raise FsmError(
                            'The dictionnary is not nondeterministic'
                        )
                    for s in t:
                        if s not in Q:
                            raise FsmError(
                                '%s is not in the set of states' % t
                            )

    @property
    def states(self):
        """Returns the list of states."""
        return self._states

    @property
    def symbols(self):
        """Returns the input alphabet."""
        return self._symbols

    @property
    def transitions(self):
        """Returns the transitions."""
        return self._transitions

    @property
    def initial_state(self):
        """Returns the initial state."""
        return self._initial_state

    @property
    def final_states(self):
        """Returns the accept states."""
        return self._final_states

    def tabulate(self, tablefmt='grid'):
        """
        Returns the state-transition table formated with the
        tabulate library.

        - The initial state is indicated with an arrow: ->
        - The accept states are indicated with a star: *

        You can choose the table format with the tablefmt argument
        (default: 'grid').

        See: https://github.com/astanin/python-tabulate
        """

        # Create headers with symbols
        headers = sorted(self._symbols)
        # Create table and index
        table, index = [], []
        for state in sorted(self._states):
            # Add line to table
            if state in self._transitions:
                line = []
                for symbol in headers:
                    if symbol in self._transitions[state]:
                        line.append(str(self._transitions[state][symbol]))
                    else:
                        line.append('{}')
                table.append(line)
            else:
                table.append(['{}'] * len(self._symbols))

            # Add state to index
            s = str(state)
            if state in self._final_states:
                s = '* ' + s
            if state == self._initial_state:
                s = '-> ' + s
            index.append(s)

        return tabulate(
            table,
            headers=headers,
            tablefmt=tablefmt,
            showindex=index,
            stralign='right'
        )

    def print_table(self):
        """
        Prints the state-transition table.
        It uses the tabulate library.

        - The initial state is indicated with an arrow: ->
        - The accept states are indicated with a star: *
        """
        print(self.tabulate())

    def delta(self, state, symbol):
        """
        State-transition function.
        It returns the next state from a state and a symbol.
        It returns {} if there is no transition.
        """
        if state not in self._states:
            raise FsmError('%s is not a state' % state)
        if symbol not in self._symbols:
            raise FsmError('%s is not a symbol' % symbol)
        if state in self._transitions and symbol in self._transitions[state]:
            return self._transitions[state][symbol]
        return None if self._is_deterministic else {}

    def dot_graph(self):
        """
        Returns the dot graph representing the automata.

        It uses the pygraphviz library. The method returns an AGraph.
        You can use the write method to write the dot graph to a file.

        See: https://pygraphviz.github.io/
        """
        # Init graph
        G = pgv.AGraph(
            name='FSM', strict=True, directed=True
        )
        G.graph_attr['rankdir'] = 'LR'
        G.node_attr['shape'] = 'circle'

        # Init nodes
        G.add_node('null', shape='point')
        G.add_nodes_from(self._states)

        # Initial state
        G.add_edge('null', self._initial_state)

        # Final states
        G.add_nodes_from(self._final_states, shape='doublecircle')

        # Transitions
        for u in self._transitions:
            for s in self._transitions[u]:
                v = self._transitions[u][s]
                if isinstance(v, Iterable) and not isinstance(v, str):
                    for node in v:
                        if G.has_edge(u, node):
                            edge = G.get_edge(u, node)
                            edge.attr['label'] += ', ' + str(s)
                        else:
                            G.add_edge(u, node, label=str(s))
                else:
                    if G.has_edge(u, v):
                        edge = G.get_edge(u, v)
                        edge.attr['label'] += ', ' + str(s)
                    else:
                        G.add_edge(u, v, label=str(s))
        return G
