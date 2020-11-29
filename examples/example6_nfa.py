"""
Example 6: NFA
--------------

An example of a nondeterministic finite automaton which has epsilon-moves.
We calculate the epsilon closure of each state.
The NFA is converted into a DFA using the powerset construction.

Graphs:
- graph6_nfa.dot
- graph6_dfa.dot

Source: https://en.wikipedia.org/wiki/Powerset_construction#Example
"""
from fsmdot.nfa import Nfa

Q = {1, 2, 3, 4}
S = {Nfa.EPSILON, '0', '1'}
d = {
    1: {
        Nfa.EPSILON: {3},
        '0': {2}
    },
    2: {
        '1': {2, 4}
    },
    3: {
        Nfa.EPSILON: {2},
        '0': {4}
    },
    4: {
        '0': {3}
    }
}
q0 = 1
F = {3, 4}

a = Nfa(Q, S, d, q0, F)
a.print_table()

G = a.dot_graph()
G.write('graph6_nfa.dot')

# Calculations of epsilon closure
for state in Q:
    print(state, a.epsilon_closure(state))

# Conversion to DFA
dfa = a.to_dfa()
dfa.print_table()
G2 = dfa.dot_graph()
G2.write('graph6_dfa.dot')
