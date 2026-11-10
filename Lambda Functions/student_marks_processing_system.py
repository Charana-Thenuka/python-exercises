'''
    Complete these tasks:
        1. Use filter() to select students who passed (marks greater than or equal to 50).
        2. Use map() to increase every mark by 5 bonus points.
        3. Use map() to convert all marks into strings with a " Marks" suffix.
        4. Display the original marks and the processed results separately.
'''

marks = [35, 75, 45, 90, 60, 25, 85, 50];

# 1. Use filter() to select students who passed (marks greater than or equal to 50).
passed_students = list(filter(lambda number : number > 50, marks));
print("Passed Students List: ", passed_students);

# 2. Use map() to increase every mark by 5 bonus points.
bonus_points = list(map(lambda number : number + 5, marks));
print("With Bonus 5 points: ", bonus_points);

# 3. Use map() to convert all marks into strings with a " Marks" suffix.
marks_string = list(map(lambda mark: str(mark) + " Marks", marks));
print(marks_string);

# 4. Display the original marks and the processed results separately.
