marks4 = {1, 2, 3}
marks5 = {1, 2, 3,4}
total_marks = sum(marks4 | marks5)  # Union of the two sets
print(total_marks)  # Output: 23

marks4 = {1, 2, 3, 4, 6, 7}
marks5 = {1, 2, 3, 4, 6, 7}
total_marks = sum(list(marks4) + list(marks5))  # Convert to lists and concatenate
print(total_marks)  # Output: 46 (sum with duplicates included)

