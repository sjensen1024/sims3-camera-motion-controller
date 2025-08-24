from decimal import Decimal

class Action:
    def __init__(self, run_at_this_many_seconds_in, method_to_call):
        self.run_at_this_many_seconds_in = Decimal(str(run_at_this_many_seconds_in))
        self.method_to_call = method_to_call
    
    def run(self):
        print(f"Running {str(self.method_to_call)} at {self.run_at_this_many_seconds_in} seconds")
        self.method_to_call()
        