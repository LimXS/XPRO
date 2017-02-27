#coding=utf-8
import pytest
from datetime import datetime, timedelta

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.mark.xfail(("6*9", 42)),
])


def test_eval(test_input, expected):
    assert eval(test_input) == expected



testdata = [
(datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
(datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


