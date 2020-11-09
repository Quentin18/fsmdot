"""
Example 7: NFA
--------------

An example of a nondeterministic finite automaton.
The NFA is converted into a DFA using the powerset construction.

Graphs:
- graph7_nfa.dot
- graph7_dfa.dot

Source:
https://en.wikipedia.org/wiki/Powerset_construction#/media/File:NFA_and_blown-up_equivalent_DFA_01.svg
"""
from fsmdot.nfa import Nfa

Q = ['X', '0', '1', '2', '3']
S = ['0', '1']
T = [
    [{'X'}, {'X', '0'}],
    [{'1'}, {'1'}],
    [{'2'}, {'2'}],
    [{'3'}, {'3'}],
    [{}, {}]
]
q0 = 'X'
F = {'3'}

a = Nfa(Q, S, T, q0, F)
a.print_table()

G = a.dot_graph()
G.write('graph7_nfa.dot')

# Conversion to DFA
dfa = a.to_dfa()
dfa.print_table()
G2 = dfa.dot_graph()
G2.write('graph7_dfa.dot')
