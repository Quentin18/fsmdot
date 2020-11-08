# https://en.wikipedia.org/wiki/Powerset_construction
from fsmdot.nfa import nfa

Q = [1, 2, 3, 4]
S = [nfa.EPSILON, '0', '1']
T = [
    [{3}, {2}, {}],
    [{}, {}, {2, 4}],
    [{2}, {4}, {}],
    [{}, {3}, {}]
]
q0 = 1
F = {3, 4}

a = nfa(Q, S, T, q0, F)
a.print_table()

G = a.dot_graph()
# print(G.to_string())
G.write('nfa2.dot')

for state in Q:
    print(state, a.epsilon_closure(state))

dfa = a.to_dfa()
dfa.print_table()
G2 = dfa.dot_graph()
G2.write('dfa2.dot')
