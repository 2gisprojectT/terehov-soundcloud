__author__ = 'Alexey'


class Action:
    def execute(self):
        pass

class EatingAction(Action):
    def execute(self):
        print "Lion is eating! Nyam nyam :3"

class SleepingAction(Action):
    def execute(self):
        print "Lion sleeps. ZzzZzzZzzZzz..."

class RunningAction(Action):
    def execute(self):
        print "Run run run, Lion!"

class LookingAction(Action):
    def execute(self):
        print "Lion is looking: beautiful!"

eating_action = EatingAction()
sleeping_action = SleepingAction()
running_action = RunningAction()
looking_action = LookingAction()