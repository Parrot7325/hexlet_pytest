"""Tests working stack in lists"""


def test_stack():
    """Tests adding"""
    stack = []
    stack.append('one')
    stack.append('two')
    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_stack1():
    """Tests extraction"""
    stack = []
    stack.append('one')
    stack.append('two')
    assert stack.pop() == 'two'


def test_stack2():
    """Tests sequence of extraction"""
    stack = []
    stack.append('one')
    stack.append('two')
    stack.pop()
    assert stack.pop() == 'one'
