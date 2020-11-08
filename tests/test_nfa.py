"""
Tests for the nfa class.

Automatons are inspired by Wikipedia:
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
"""
import pytest
from fsmdot.nfa import nfa


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
    return nfa(Q, S, T, q0, F)


@pytest.fixture
def a2():
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
    return nfa(Q, S, T, q0, F)


def test_delta(a1, a2):
    assert a1.delta('p', '0') == {'p'}
    assert a1.delta('p', '1') == {'p', 'q'}
    assert a1.delta('q', '0') == {}
    assert a1.delta('q', '1') == {}

    assert a2.delta('S0', '0') == {}
    assert a2.delta('S0', '1') == {}
    assert a2.delta('S0', nfa.EPSILON) == {'S1', 'S3'}
    assert a2.delta('S1', '0') ==  {'S2'}
    assert a2.delta('S1', '1') == {'S1'}
    assert a2.delta('S1', nfa.EPSILON) == {}
    assert a2.delta('S2', '0') == {'S1'}
    assert a2.delta('S2', '1') == {'S2'}
    assert a2.delta('S2', nfa.EPSILON) == {}
    assert a2.delta('S3', '0') == {'S3'}
    assert a2.delta('S3', '1') == {'S4'}
    assert a2.delta('S3', nfa.EPSILON) == {}
    assert a2.delta('S4', '0') == {'S4'}
    assert a2.delta('S4', '1') == {'S3'}
    assert a2.delta('S4', nfa.EPSILON) == {}


def test_accept(a1, a2):
    assert not a1.accept('11110')
    assert a1.accept('110110110101')

    # assert a2.accept('1001')
    # assert a2.accept('10101')
    assert not a2.accept('10')
    assert not a2.accept('01')
