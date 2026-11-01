from student import students
from utils.helper import (
    get_highest_score,
    get_lowest_score,
    calculate_average
)

print("====== STUDENT REPORT ======")

for student in students:
    print(f"{student['name']} : {student['score']}")

print("\nStatistics")

print(f"Highest Score: {get_highest_score(students)}")
print(f"Lowest Score: {get_lowest_score(students)}")
print(f"Average Score: {calculate_average(students):.2f}")
