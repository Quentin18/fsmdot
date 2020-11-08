from fsmdot.dfa import dfa

Q = ['S1', 'S2']
S = ['0', '1']
q0 = 'S1'
F = {'S1'}
T = [
    ['S2', 'S1'],
    ['S1', 'S2']
]

a = dfa(Q, S, T, q0, F)
a.print_table()

print(a.accept('11110'))
print(a.accept('110110110101'))

G = a.dot_graph()
print(G.to_string())
G.write('dfa.dot')
