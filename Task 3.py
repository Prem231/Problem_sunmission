marks = [54, 87, 43, 85, 90, 43, 12, 56, 76, 43, 87, 54, 65, 76, 89, 73, 32]
passed_marks = []
for mark in marks:
    if mark > 60:
        passed_marks.append(mark)
print("Passed Marks:")
for mark in passed_marks:
    print(mark)