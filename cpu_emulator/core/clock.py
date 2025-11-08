# Clock and log file
class Clock:
    def __init__(self, cpu, log_file_path=None):
        self.state = 0
        self.on = True
        self.log_file_path = log_file_path

    def advance(self, cpu):
        # Save the state in the log file (only if log_file_path is set)
        if self.log_file_path is not None:
            if self.state == 0:
                # Create the file at first
                with open(self.log_file_path, "w") as log_file:
                    log_file.write(f"{cpu}\n")
            else: 
                # Update the file
                with open(self.log_file_path, "a") as log_file:
                    log_file.write(f"{cpu}\n")
            
        # Make the clock click
        self.state += 1

    def __str__(self):
        return str(self.state)
    

# RingCounter: periodic counter to control the execution of microinstructions
class RingCounter():
	def __init__(self, n_time_states):
		self.state=0
		self.n_time_states=n_time_states

	def advance(self):
		self.state=(self.state+1)%self.n_time_states
	
	def read(self):
		return self.state
		
	def __str__(self):
		return str(self.state)

