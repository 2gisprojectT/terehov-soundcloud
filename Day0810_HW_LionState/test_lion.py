import random
from Day0810_HW_LionState.inputs import input_hunter, input_antelope, input_tree
from Day0810_HW_LionState.lion import Lion
from Day0810_HW_LionState.states import fed_state, hungry_state

__author__ = 'Alexey'

import unittest


class LionTest(unittest.TestCase):
    def test_creating_of_lion(self):
        self.assertRaises(ValueError, Lion, 1)
        self.assertRaises(ValueError, Lion, None)
        try:
            Lion(fed_state)
        except ValueError:
            self.fail("Unexpectedly error on creating Lion with correct param")
        try:
            Lion(hungry_state)
        except ValueError:
            self.fail("Unexpectedly error on creating Lion with correct param")

    def test_giving_correct_inputs(self):
        correct_inputs = [input_antelope, input_hunter, input_tree]
        lion = Lion(hungry_state)
        try:
            for i in range(0, 100):
                index = random.randint(0, len(correct_inputs) - 1)
                lion.take_it(correct_inputs[index])
        except:
            self.fail("Error on correct input")
        lion = Lion(hungry_state)
        try:
            for i in range(0, 100):
                index = random.randint(0, len(correct_inputs) - 1)
                lion.take_it(correct_inputs[index])
        except:
            self.fail("Error on correct input")

    def test_giving_wrong_inputs(self):
        wrong_inputs = [None, "Devil", 666, object()]
        lion = Lion(hungry_state)
        for i in wrong_inputs:
            self.assertRaises(ValueError, lion.take_it, i)

    def test_transitions(self):
        correct_transitions = {
            (hungry_state, input_antelope): fed_state,
            (hungry_state, input_hunter): hungry_state,
            (hungry_state, input_tree): hungry_state,
            (fed_state, input_antelope): hungry_state,
            (fed_state, input_hunter): hungry_state,
            (fed_state, input_tree): hungry_state
        }
        msg = "Incorrect state"
        for st, inp in correct_transitions:
            lion = Lion(st)
            self.assertEqual(lion.current_state, st, msg)
            lion.take_it(inp)
            self.assertEqual(lion.current_state, correct_transitions[(st, inp)], msg)