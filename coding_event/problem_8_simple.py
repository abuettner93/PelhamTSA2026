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

import pandas as pd
df = pd.read_csv("p8_data.csv")
#average score per event
print(df.groupby('event')['score'].mean())
#highest-scoring student overall
print(df.groupby('name')['score'].sum())

print(df)




