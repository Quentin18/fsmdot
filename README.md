# Finite-state machines with dot

**fsmdot** is a Python package to create finite-state machines which can be exported to dot. It uses the [pygraphviz](https://pygraphviz.github.io/) library which is a Python interface to the [Graphviz](https://graphviz.org/) graph layout and visualization package.

## Installing
- First, you need to install Graphviz. See how to download it [here](https://graphviz.org/download/).
- Then, *fsmdot* can be installed using [pip](https://pip.pypa.io/en/stable/):
```
pip3 install fsmdot
```

## Usage
With the *fsmdot* library, you can create two different types of finite-state machine:
- **Deterministic finite automaton** (DFA)
- **Nondeterministic finite automaton** (NFA)

A finite-state machine is represented by a quintuple (Q, S, T, q0, F) where:
- **Q** is a list of states
- **S** is the input alphabet (a list of symbols)
- **T** is the state-transition table
- **q0** is the initial state, an element of Q
- **F** is the set of accept states

The order of states and symbols is important in Q and S
to make the state-transition table.

### Deterministic finite automaton
Example:
```python
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
```

### Nondeterministic finite automaton
Example:
```python
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
```

## References
- [Automata theory](https://en.wikipedia.org/wiki/Automata_theory)
- [Finite-state machines](https://en.wikipedia.org/wiki/Finite-state_machine)
- [Deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)
- [Nondeterministic finite automaton](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
- [Powerset construction](https://en.wikipedia.org/wiki/Powerset_construction)
- [DFA minimization](https://en.wikipedia.org/wiki/DFA_minimization)

## Author
[Quentin Deschamps](mailto:quentindeschamps18@gmail.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)
