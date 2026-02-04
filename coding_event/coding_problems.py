# Problem 2
# list of tuples, where each tuple is (gpa,attendance,safety)
students = [
    ("Bob", 3.5, 90, "yes"),
    ("Suzie", 2.5, 50, "no"),
    ("Jim", 3.0, 90, "yes"),
    ("Tom", 2.2, 75, "yes")
]

eligible_list = [student[0] for student in students if student[1] >= 2.5 and student[2] >= 90 and student[3] == "yes"]
print(eligible_list)
print(f"There are {len(eligible_list)} students eligible")

exit()

eligible_students = 0
for student in students:
    name, gpa, attendance, safety = student
    if gpa >= 2.5 and attendance >= 90 and safety == "yes":
        print(f"{name} is eligible")
        eligible_students += 1
    else:
        print(f"{name} is not eligible")

print(f"There {'is' if eligible_students ==1 else 'are'} {eligible_students} eligible student(s)")
