"""
Example 4: NFA
--------------

An example of a nondeterministic finite automaton which requires that
the input contains 'aaa'.

Graph: graph4_nfa.dot
"""
from fsmdot.nfa import Nfa

Q = {0, 1, 2, 3}
S = {'a', 'b'}
d = {
    0: {
        'a': {0, 1},
        'b': {0}
    },
    1: {
        'a': {2}
    },
    2: {
        'a': {3}
    },
    3: {
        'a': {3},
        'b': {3}
    }
}
q0 = 0
F = {3}

a = Nfa(Q, S, d, q0, F)
a.print_table()

print(a.accept('ababaaabaaaaabababa'))
print(a.accept('abababaa'))

G = a.dot_graph()
print(G.to_string())
G.write('graph4_nfa.dot')
