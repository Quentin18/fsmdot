"""
Example 3: NFA
--------------

An example of a nondeterministic finite automaton, with a binary alphabet,
which determines if the input ends with a 1.

Graph: graph3_nfa.dot

Source: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton#Example
"""
from fsmdot.nfa import Nfa

Q = ['p', 'q']
S = ['0', '1']
T = [
    [{'p'}, {'p', 'q'}],
    [{}, {}]
]
q0 = 'p'
F = {'q'}

a = Nfa(Q, S, T, q0, F)
a.print_table()

print(a.accept('11110'))
print(a.accept('110110110101'))

G = a.dot_graph()
print(G.to_string())
G.write('graph3_nfa.dot')
