import pytest
from fsmdot.dfa import dfa


@pytest.fixture
def automata():
    Q = ['S1', 'S2']
    S = ['0', '1']
    T = [
        ['S2', 'S1'],
        ['S1', 'S2']
    ]
    q0 = 'S1'
    F = {'S1'}
    return dfa(Q, S, T, q0, F)


def test_accept(automata):
    assert not automata.accept('11110')
    assert automata.accept('110110110101')
