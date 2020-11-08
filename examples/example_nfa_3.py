from fsmdot.nfa import nfa

Q = ['S0', 'S1', 'S2', 'S3', 'S4']
S = ['0', '1', nfa.EPSILON]
T = [
    [{}, {}, {'S1', 'S3'}],
    [{'S2'}, {'S1'}, {}],
    [{'S1'}, {'S2'}, {}],
    [{'S3'}, {'S4'}, {}],
    [{'S4'}, {'S3'}, {}],
]
q0 = 'S0'
F = {'S1', 'S3'}

a = nfa(Q, S, T, q0, F)
a.print_table()

G = a.dot_graph()
G.write('nfa3.dot')
