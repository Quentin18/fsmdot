"""
Example 1: DFA
--------------

The following example is of a DFA, with a binary alphabet, which requires that
the input contains an even number of 0s

Graph: graph1_dfa.dot

Source: https://en.wikipedia.org/wiki/Deterministic_finite_automaton#Example
"""
from fsmdot.dfa import Dfa

Q = {'S1', 'S2'}
S = {'0', '1'}
d = {
    'S1': {
        '0': 'S2',
        '1': 'S1'
    },
    'S2': {
        '0': 'S1',
        '1': 'S2'
    }
}
q0 = 'S1'
F = {'S1'}

a = Dfa(Q, S, d, q0, F)
a.print_table()

print(a.accept('11110'))
print(a.accept('110110110101'))

G = a.dot_graph()
print(G.to_string())
G.write('graph1_dfa.dot')
