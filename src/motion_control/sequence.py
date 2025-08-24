import time
from decimal import Decimal

class Sequence:
    def __init__(self, duration_in_seconds):
        self.duration_in_seconds = duration_in_seconds
        if self.duration_in_seconds <= 0:
            print("duration_in_seconds must be greater than 0. The passed-in one isn't, so we're setting it to 10.")
            self.duration_in_seconds = 10
        self.duration_in_seconds = Decimal(str(self.duration_in_seconds))
        self.actions = []
        self.actions_per_increment = []
        self.increment_in_seconds = Decimal("0.5")

    def add_action(self, action):
        self.actions.append(action)

    def run(self):
        self.__setup_actions_per_increment()
        total_increments = 0
        index_counter = 0
        while total_increments <= self.duration_in_seconds:
            if total_increments == 0:
                print("Starting sequence!")
            print(f"{total_increments} second mark...")
            self.__run_action_at_increment_index(index_counter)
            time.sleep(self.increment_in_seconds)
            total_increments += self.increment_in_seconds
            index_counter += 1
        print("Sequence finished!")

    def __setup_actions_per_increment(self):
        total_increments = 0
        index_counter = 0
        while total_increments <= self.duration_in_seconds:
            actions_at_this_increment = []
            for action in self.actions:
                if action.run_at_this_many_seconds_in == total_increments:
                    actions_at_this_increment.append(action)
            self.actions_per_increment.append(actions_at_this_increment)
            total_increments += self.increment_in_seconds
            index_counter += 1

    def __run_action_at_increment_index(self, index):
        actions = self.actions_per_increment[index]
        [action.run() for action in actions]
