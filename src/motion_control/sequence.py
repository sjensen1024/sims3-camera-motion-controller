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
        self.action_timings = []
        self.increment_in_seconds = Decimal("0.5")

    def add_action(self, action):
        self.actions.append(action)

    def run(self):
        self.__setup_action_timings()
        total_increments = 0
        index_counter = 0
        while total_increments <= self.duration_in_seconds:
            if total_increments == 0:
                print("Starting sequence!")
            print(f"{total_increments} second mark...")
            self.__run_action_timing_at_index(index_counter)
            time.sleep(self.increment_in_seconds)
            total_increments += self.increment_in_seconds
            index_counter += 1
        print("Sequence finished!")

    def __setup_action_timings(self):
        total_increments = 0
        index_counter = 0
        while total_increments <= self.duration_in_seconds:
            self.action_timings.append(None)
            for action in self.actions:
                if action.run_at_this_many_seconds_in == total_increments:
                    self.action_timings[index_counter] = action
            total_increments += self.increment_in_seconds
            index_counter += 1

    def __run_action_timing_at_index(self, index):
        action = self.action_timings[index]
        if action is None:
            return
        action.run()
