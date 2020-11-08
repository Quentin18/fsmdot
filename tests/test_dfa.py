"""
Tests for the dfa class.

Automatons are inspired by Wikipedia:
https://en.wikipedia.org/wiki/Deterministic_finite_automaton
"""
import pytest
from fsmdot.dfa import dfa


@pytest.fixture
def a1():
    Q = ['S1', 'S2']
    S = ['0', '1']
    T = [
        ['S2', 'S1'],
        ['S1', 'S2']
    ]
    q0 = 'S1'
    F = {'S1'}
    return dfa(Q, S, T, q0, F)


@pytest.fixture
def a2():
    Q = ['S0', 'S1', 'S2']
    S = ['0', '1']
    T = [
        ['S0', 'S1'],
        ['S2', 'S0'],
        ['S1', 'S2']
    ]
    q0 = 'S0'
    F = {'S0'}
    return dfa(Q, S, T, q0, F)


def test_delta(a1, a2):
    assert a1.delta('S1', '0') == 'S2'
    assert a1.delta('S2', '0') == 'S1'
    assert a1.delta('S1', '1') == 'S1'
    assert a1.delta('S2', '1') == 'S2'

    assert a2.delta('S0', '0') == 'S0'
    assert a2.delta('S0', '1') == 'S1'
    assert a2.delta('S1', '0') == 'S2'
    assert a2.delta('S1', '1') == 'S0'
    assert a2.delta('S2', '0') == 'S1'
    assert a2.delta('S2', '1') == 'S2'


def test_accept(a1, a2):
    assert not a1.accept('11110')
    assert a1.accept('110110110101')

    assert a2.accept('1001')
    assert a2.accept('10101')
    assert a2.accept('11100010100')
    assert not a2.accept('101')
    assert not a2.accept('1110')
