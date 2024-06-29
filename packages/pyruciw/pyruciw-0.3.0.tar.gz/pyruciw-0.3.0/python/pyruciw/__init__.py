__all__ = ["hello"]

import pyruciw

# Create an environment
env = pyruciw.Environment()

# Schedule some events
env.schedule_event(pyruciw.Event(time=0.0, event_type=pyruciw.EventType.Arrival))
env.schedule_event(pyruciw.Event(time=1.0, event_type=pyruciw.EventType.Service))

# Run the simulation
env.run_until(10.0)

# Get the queue length
print(env.get_queue_length())

# Use the simulate_queue function
lengths = pyruciw.simulate_queue(arrival_rate=1.0, service_rate=2.0, end_time=10.0)
print(lengths)

