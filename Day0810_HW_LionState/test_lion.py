from Day0810_HW_LionState.inputs import input_hunter
from Day0810_HW_LionState.lion import Lion
from Day0810_HW_LionState.states import fed_state, hungry_state

__author__ = 'Alexey'

import unittest


class LionTest(unittest.TestCase):
    def test_lion(self):
        l = Lion(fed_state)
        l.take_it(input_hunter)
        self.assertEqual(l.current_state, hungry_state, "Lion should be hungry!")