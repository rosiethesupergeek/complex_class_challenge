from lib.counter import *

def test_counter():
    counting = Counter()
    counting.add(9)
    result = counting.report()
    assert result == "Counted to 9 so far."

def test_add():
    counting = Counter()
    counting.add(8)
    result = counting.report()
    assert result == "Counted to 8 so far."

def test_multiple_add():
    counting = Counter()
    counting.add(5)
    counting.add(7)
    counting.add(50)
    result = counting.report()
    assert result == 'Counted to 62 so far.'

def test_negative():
    counting = Counter()
    counting.add(-5)
    result = counting.report()
    assert result == 'Counted to -5 so far.'