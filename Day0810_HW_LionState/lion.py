from Day0810_HW_LionState.actions import sleeping_action, running_action, looking_action, eating_action
from Day0810_HW_LionState.inputs import input_tree, input_antelope, input_hunter
from Day0810_HW_LionState.states import State, hungry_state, fed_state

__author__ = 'Alexey'


class Lion:
    def __init__(self, start_state):
        self.current_state = start_state
        self.table = {
            (fed_state, input_antelope): (sleeping_action, hungry_state),
            (fed_state, input_hunter): (running_action, hungry_state),
            (fed_state, input_tree): (looking_action, hungry_state),
            (hungry_state, input_antelope): (eating_action, fed_state),
            (hungry_state, input_hunter): (running_action, None),
            (hungry_state, input_tree): (sleeping_action, None)
        }

    def take_it(self, something):
        if (self.current_state, something) not in self.table:
            print "Wrong input!"
        action, next_state = self.table[(self.current_state, something)]
        if action is not None:
            action.execute()
        if next_state is not None:
            self.current_state = next_state