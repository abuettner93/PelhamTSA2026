# 8. File-Based Problems (Advanced / Finals-Level)
# At higher levels, students may read from files.
# Example 8: CSV Processing
# Input file:
#  StudentName, Event, Score
# Tasks:
# Average score per event
# Highest-scoring student overall
# Output summary table
# Skills tested
# File I/O
# Parsing
# Aggregation
# Sorting

# ---- Step 1: Read the CSV file ----
# open() gives us access to the file, "r" means read mode
# We use a list to store each row as a dictionary for easy access
rows = []
file = open("p8_data.csv", "r")
lines = file.readlines()
file.close()


# The first line is the header — skip it, start from index 1
column_names = lines[0].strip().split(",")
for line in lines[1:]:
    line = line.strip()             # remove newline and extra whitespace
    if line == "":                  # skip blank lines
        continue
    parts = line.split(",")        # split on commas: ["Alex", "Math", "90"]
    name = parts[0]
    event = parts[1]
    score = int(parts[2])
    rows.append({column_names[0]: name,
                 column_names[1]: event,
                 column_names[2]: score}
                )

print(rows)

# ---- Step 2: Average score per event ----
# We need to group scores by event, then average each group
# Use a dictionary: key = event name, value = list of scores
scores_by_event = {}
for row in rows:
    event = row["event"]
    if event not in scores_by_event:
        scores_by_event[event] = []
    scores_by_event[event].append(row["score"])

print(scores_by_event)

print("=== Average Score Per Event ===")
for event, scores in scores_by_event.items():
    average = sum(scores) / len(scores)
    print(f"  {event}: {average:.1f}")


# ---- Step 3: Highest-scoring student overall ----
# Add up each student's scores across all events
totals_by_student = {}
for row in rows:
    name = row["name"]
    if name not in totals_by_student:
        totals_by_student[name] = 0
    totals_by_student[name] += row["score"]

print(totals_by_student)

# Find the student with the highest total
best_student = ""
best_total = 0
for name, total in totals_by_student.items():
    if total > best_total:
        best_student = name
        best_total = total

print(f"\n=== Highest-Scoring Student ===")
print(f"  {best_student} with a total of {best_total}")

# ---- Step 4: Output summary table ----
# Show every row neatly, sorted by student name then event
# sorted() with a key function lets us control the sort order
sorted_rows = sorted(rows, key=lambda r: (r["event"], r["score"]))

print(sorted_rows)

print(f"\n=== Full Summary Table ===")
print(f"  {'Student':<12} {'Event':<10} {'Score':>5}")
print(f"  {'-' * 12} {'-' * 10} {'-' * 5}")
for row in sorted_rows:
    print(f"  {row['name']:<12} {row['event']:<10} {row['score']:>5}")
