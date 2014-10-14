import random
from Day1008_HW_LionState.inputs import input_hunter, input_antelope, input_tree
from Day1008_HW_LionState.lion import Lion
from Day1008_HW_LionState.states import fed_state, hungry_state

__author__ = 'Alexey'

import unittest


class LionTest(unittest.TestCase):
    def test_constructor_for_exceptions(self):
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

    def test_constructor_functionality(self):
        hungry_lion = Lion(hungry_state)
        fed_lion = Lion(fed_state)
        msg = "Wrong constructor functionality"
        self.assertEqual(hungry_lion.current_state, hungry_state, msg)
        self.assertEqual(fed_lion.current_state, fed_state, msg)

    def test_hungry_lion_for_exceptions(self):
        lion = Lion(hungry_state)
        try:
            # hungry state
            lion.take_it(input_hunter)
            lion.take_it(input_tree)
            # fed state
            lion.take_it(input_antelope)
            lion.take_it(input_antelope)
            lion.take_it(input_antelope)
            lion.take_it(input_hunter)
            lion.take_it(input_antelope)
            lion.take_it(input_tree)
        except:
            self.fail("Error in hungry lion")

    def test_fed_lion_for_exceptions(self):
        lion = Lion(fed_state)
        try:
            # fed state
            lion.take_it(input_hunter)
            lion.take_it(input_antelope)
            lion.take_it(input_tree)
            lion.take_it(input_antelope)
            lion.take_it(input_antelope)
            # hungry state
            lion.take_it(input_hunter)
            lion.take_it(input_tree)
        except:
            self.fail("Error in fed lion")

    def test_giving_wrong_inputs(self):
        wrong_inputs = [None, "Devil", 666, object()]
        hungry_lion = Lion(hungry_state)
        fed_lion = Lion(fed_state)
        for i in wrong_inputs:
            self.assertRaises(ValueError, hungry_lion.take_it, i)
            self.assertRaises(ValueError, fed_lion.take_it, i)

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