# Example 3: Workshop Scheduling
# Problem:
#  A lab has 3 machines. Each job has a required time.
# Rules:
# One job per machine at a time
# No preemption
# Task:
#  Assign jobs in order and compute:
# Total completion time
# Idle time for each machine
# Skills tested
# Simulation logic
# Arrays
# Tracking state over time

# Each job is a tuple: (job_name, time_required)
jobs = [
    ("Job A", 4),
    ("Job B", 2),
    ("Job C", 5),
    ("Job D", 1),
    ("Job E", 3),
    ("Job F", 6),
    ("Job G", 2)
]

NUM_MACHINES = 3

# Track when each machine becomes available (starts at time 0)
# This array holds the "finish time" of whatever job is currently on each machine
machine_available_at = [0, 0, 0]

# Track which jobs each machine runs (for display purposes)
machine_jobs = [[] for _ in range(NUM_MACHINES)]

# --- Assign jobs in order to whichever machine is free earliest ---
# "In order" means we go through the job list sequentially.
# For each job, we pick the machine with the smallest available time.
# This is a classic greedy scheduling approach (Longest Processing Time isn't
# required here — we just assign in the given order).

for job_name, job_time in jobs:
    # Find the machine that becomes free the earliest
    earliest_machine = 0
    for i in range(1, NUM_MACHINES):
        if machine_available_at[i] < machine_available_at[earliest_machine]:
            earliest_machine = i

    # Record the start and end time for this job on the chosen machine
    start_time = machine_available_at[earliest_machine]
    end_time = start_time + job_time

    # Update the machine's available time
    machine_available_at[earliest_machine] = end_time

    # Log the assignment
    machine_jobs[earliest_machine].append((job_name, start_time, end_time))
    print(f"{job_name} (time={job_time}) -> Machine {earliest_machine + 1} "
          f"[starts at t={start_time}, ends at t={end_time}]")

# --- Compute results ---

# Total completion time is when the LAST machine finishes (the makespan)
total_completion_time = max(machine_available_at)

# Idle time for each machine = total_completion_time - time spent working
# Time spent working = sum of all job durations assigned to that machine
print("\n--- Results ---")
for i in range(NUM_MACHINES):
    busy_time = sum(end - start for _, start, end in machine_jobs[i])
    idle_time = total_completion_time - busy_time
    job_names = [name for name, _, _ in machine_jobs[i]]
    print(f"Machine {i + 1}: Jobs {job_names}, "
          f"Busy={busy_time}, Idle={idle_time}")

print(f"\nTotal completion time (makespan): {total_completion_time}")
