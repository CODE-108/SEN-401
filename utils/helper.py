def get_highest_score(students):
    return max(student["score"] for student in students)

def get_lowest_score(students):
    return min(student["score"] for student in students)

def calculate_average(students):
    total = sum(student["score"] for student in students)
    return total / len(students)