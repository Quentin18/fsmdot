"""
Example 5: NFA
--------------

An example of a nondeterministic finite automaton which has epsilon-moves,
with a binary alphabet, that determines if the input contains an even
number of 0s or an even number of 1s.

Graph: graph5_nfa.dot

Source:
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton#Example_2
"""
from fsmdot.nfa import Nfa

Q = ['S0', 'S1', 'S2', 'S3', 'S4']
S = ['0', '1', Nfa.EPSILON]
T = [
    [{}, {}, {'S1', 'S3'}],
    [{'S2'}, {'S1'}, {}],
    [{'S1'}, {'S2'}, {}],
    [{'S3'}, {'S4'}, {}],
    [{'S4'}, {'S3'}, {}],
]
q0 = 'S0'
F = {'S1', 'S3'}

a = Nfa(Q, S, T, q0, F)
a.print_table()

for string in ['1001', '10101', '10', '01']:
    print(a.accept(string))

G = a.dot_graph()
G.write('graph5_nfa.dot')
