"""
Example 2: DFA
--------------

An example of a deterministic finite automaton that accepts only binary
numbers that are multiples of 3.

Graph: graph2_dfa.dot

Source:
https://en.wikipedia.org/wiki/Deterministic_finite_automaton#/media/File:DFA_example_multiplies_of_3.svg
"""
from fsmdot.dfa import Dfa

Q = ['S0', 'S1', 'S2']
S = ['0', '1']
T = [
    ['S0', 'S1'],
    ['S2', 'S0'],
    ['S1', 'S2']
]
q0 = 'S0'
F = {'S0'}

a = Dfa(Q, S, T, q0, F)
a.print_table()

print(a.accept('1001'))

G = a.dot_graph()
print(G.to_string())
G.write('graph2_dfa.dot')
