# Problem:
#  Temperature readings recorded every minute.
# Tasks:
# Find min, max, average
# Count readings outside safe range (65–85°F)
# Output:
#  Formatted summary report.


input = [34, 56.2, 65, 87, 92.4, 18, 47, 76, 69.3, 84]

# outside_range = 0

minimum = min(input)
maximum = max(input)
average = sum(input) / len(input)

# for val in input:
#     if val < 65 or val > 85:
#         outside_range += 1

outside_range = [val for val in input if val < 65 or val > 85]

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")
print(f"Outside range: {outside_range}")