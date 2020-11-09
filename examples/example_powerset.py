# https://en.wikipedia.org/wiki/Powerset_construction
from fsmdot.nfa import nfa

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

a = nfa(Q, S, T, q0, F)
a.print_table()

G = a.dot_graph()
# print(G.to_string())
G.write('nfa4.dot')

dfa = a.to_dfa()
dfa.print_table()
G2 = dfa.dot_graph()
G2.write('dfa4.dot')
