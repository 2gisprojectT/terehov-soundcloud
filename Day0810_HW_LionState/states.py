__author__ = 'Alexey'


class State:
    def info(self):
        pass

class HungryState(State):
    def info(self):
        print "I'm so hungry!!!"

class FedState(State):
    def info(self):
        print "So fed: can't see on food anymore"

hungry_state = HungryState()
fed_state = FedState()