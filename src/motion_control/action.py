class Action:
    def __init__(self, run_at_this_many_seconds_in, caller, method_name):
        self.run_at_this_many_seconds_in = run_at_this_many_seconds_in
        self.caller = caller
        self.method_name = method_name
    
    def run(self):
        method_to_call = getattr(self.caller, self.method_name)
        print(f"Running {self.method_name} from instance of {str(self.caller.__class__)} at {self.run_at_this_many_seconds_in} seconds")
        method_to_call()
        