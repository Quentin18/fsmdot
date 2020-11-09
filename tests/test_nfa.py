"""
Tests for the Nfa class.

Automatons are inspired by Wikipedia:
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
"""
import pytest
from fsmdot.nfa import Nfa


@pytest.fixture
def a1():
    Q = ['p', 'q']
    S = ['0', '1']
    T = [
        [{'p'}, {'p', 'q'}],
        [{}, {}]
    ]
    q0 = 'p'
    F = {'q'}
    return Nfa(Q, S, T, q0, F)


@pytest.fixture
def a2():
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
    return Nfa(Q, S, T, q0, F)


@pytest.fixture
def a3():
    Q = [1, 2, 3, 4]
    S = [Nfa.EPSILON, '0', '1']
    T = [
        [{3}, {2}, {}],
        [{}, {}, {2, 4}],
        [{2}, {4}, {}],
        [{}, {3}, {}]
    ]
    q0 = 1
    F = {3, 4}
    return Nfa(Q, S, T, q0, F)


@pytest.fixture
def a4():
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
    return Nfa(Q, S, T, q0, F)


def test_has_epsilon_moves(a1, a2):
    assert not a1.has_epsilon_moves()
    assert a2.has_epsilon_moves()


def test_delta(a1, a2):
    assert a1.delta('p', '0') == {'p'}
    assert a1.delta('p', '1') == {'p', 'q'}
    assert a1.delta('q', '0') == {}
    assert a1.delta('q', '1') == {}

    assert a2.delta('S0', '0') == {}
    assert a2.delta('S0', '1') == {}
    assert a2.delta('S0', Nfa.EPSILON) == {'S1', 'S3'}
    assert a2.delta('S1', '0') == {'S2'}
    assert a2.delta('S1', '1') == {'S1'}
    assert a2.delta('S1', Nfa.EPSILON) == {}
    assert a2.delta('S2', '0') == {'S1'}
    assert a2.delta('S2', '1') == {'S2'}
    assert a2.delta('S2', Nfa.EPSILON) == {}
    assert a2.delta('S3', '0') == {'S3'}
    assert a2.delta('S3', '1') == {'S4'}
    assert a2.delta('S3', Nfa.EPSILON) == {}
    assert a2.delta('S4', '0') == {'S4'}
    assert a2.delta('S4', '1') == {'S3'}
    assert a2.delta('S4', Nfa.EPSILON) == {}


def test_accept(a1, a2):
    assert not a1.accept('11110')
    assert a1.accept('110110110101')

    assert a2.accept('1001')
    assert a2.accept('10101')
    assert not a2.accept('10')
    assert not a2.accept('01')


def test_epsilon_closure(a2):
    assert a2.epsilon_closure('S0') == {'S0', 'S1', 'S3'}
    for state in ['S1', 'S2', 'S3', 'S4']:
        assert a2.epsilon_closure(state) == {state}


def test_to_dfa(a3, a4):
    dfa3 = a3.to_dfa()
    dfa4 = a4.to_dfa()
    assert dfa3.symbols == ['0', '1']
    assert len(dfa3.states) == 4
    assert dfa4.symbols == ['0', '1']
    assert len(dfa4.states) >= 16
    assert a3.accept('011101100')
    assert dfa3.accept('011101100')
    assert a4.accept('1001011100')
    assert dfa4.accept('1001011100')
