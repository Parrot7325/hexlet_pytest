"""Tests function for reversing string"""
from example import reverse


def test_reverse():
    """Usual check"""
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    """Check for empty string"""
    assert reverse('') == ''

