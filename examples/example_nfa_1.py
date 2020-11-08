from fsmdot.nfa import nfa

Q = [0, 1, 2, 3]
S = ['a', 'b']
T = [
    [{0, 1}, {0}],
    [{2}, {}],
    [{3}, {}],
    [{3}, {3}]
]
q0 = 0
F = {3}

a = nfa(Q, S, T, q0, F)
a.print_table()

print(a.accept('ababaaabaaaaabababa'))
print(a.accept('abababaa'))

G = a.dot_graph()
print(G.to_string())
G.write('nfa.dot')
