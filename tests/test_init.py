"""
Tests for initialization of FSM.
"""
import pytest
from fsmdot.dfa import Dfa
from fsmdot.nfa import Nfa
from fsmdot.error import FsmError


def test_init_1():
    with pytest.raises(FsmError):
        Q = {'S0', 'S1', 'S2'}
        S = {'0', '1'}
        d = {
            'S0': {
                '0': 'S0',
                '1': 'S1'
            },
            'S1': {
                '0': 'S2',
                '1': 'S0'
            },
            'S2': {
                '0': 'S1',
                '1': 'S2'
            }
        }
        q0 = 'S3'   # Q does not contain q0
        F = {'S0'}
        Dfa(Q, S, d, q0, F)


def test_init_2():
    with pytest.raises(FsmError):
        Q = {'S0', 'S1', 'S2'}
        S = {'0', '1'}
        d = {
            'S0': {
                '0': 'S0',
                '1': 'S1'
            },
            'S1': {
                '0': 'S2',
                '1': 'S0'
            },
            'S2': {
                '0': 'S1',
                '1': 'S2'
            }
        }
        q0 = 'S0'
        F = {'S0', 'S3'}    # Q does not contain all states of F
        Dfa(Q, S, d, q0, F)


def test_init_3():
    with pytest.raises(FsmError):
        Q = {0, 1, 2, 3}
        S = {'a', 'b'}
        d = {
            0: {
                'a': {0, 1},
                'b': {0}
            },
            1: {
                'a': {2}
            },
            2: {
                'a': {3}
            },
            3: {
                'a': {3},
                'b': {3}
            }
        }   # the state-transition function is not deterministic
        q0 = 0
        F = {3}
        Dfa(Q, S, d, q0, F)


def test_init_4():
    with pytest.raises(FsmError):
        Q = {'S0', 'S1'}
        S = {'0', '1'}
        d = {
            'S0': {
                '0': 'S0',
                '1': 'S1'
            },
            'S1': {
                '0': 'S2',
                '1': 'S0'
            },
            'S2': {     # S2 is not in Q
                '0': 'S1',
                '1': 'S2'
            }
        }
        q0 = 'S0'
        F = {'S0'}
        Dfa(Q, S, d, q0, F)


def test_init_5():
    with pytest.raises(FsmError):
        Q = {'S0', 'S1', 'S2'}
        S = {'0', '1'}
        d = []   # d is not a dictionnary
        q0 = 'S0'
        F = {'S0'}
        Dfa(Q, S, d, q0, F)


def test_init_6():
    with pytest.raises(FsmError):
        Q = {'S0', 'S1', 'S2'}
        S = {'0'}
        d = {
            'S0': {
                '0': 'S0',
                '1': 'S1'   # 1 is not in S
            },
            'S1': {
                '0': 'S2',
                '1': 'S0'
            },
            'S2': {
                '0': 'S1',
                '1': 'S2'
            }
        }
        q0 = 'S0'
        F = {'S0'}
        Dfa(Q, S, d, q0, F)


def test_init_7():
    with pytest.raises(FsmError):
        Q = {'S0', 'S1', 'S2'}
        S = {'0', '1'}
        d = {
            'S0': {
                '0': 'S0',
                '1': 'S1'
            },
            'S1': {
                '0': 'S2',
                '1': 'S0'
            },
            'S2': {
                '0': 'S1',
                '1': 'S2'
            }
        }   # the state-transition function is not nondeterministic
        q0 = 'S0'
        F = {'S0'}
        Nfa(Q, S, d, q0, F)
