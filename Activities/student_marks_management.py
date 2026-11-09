'''
    Requirements:
    1. Create a dictionary containing at least 5 students and their marks.
    2. Display all student names and marks.
    3. Find the student with the highest marks.
    4. Find the student with the lowest marks.
    5. Calculate the average marks.
    6. Display students who scored more than 75 marks.
    7. Allow the user to search for a student by name.
'''

students = {
    "kamal": 31,
    "Nimal": 80,
    "Sunil": 76,
    "Vimal": 70,
    "Chamil": 75
}

# display all students names and marks
print(students.items());

# 3. find the student with higest mark
highest_mark = 0;
highest_mark_name = "";

for name, mark in students.items():
    if (highest_mark < mark):
        highest_mark = mark;
        highest_mark_name = name;

print("Highest Mark: ", highest_mark);
print("Name of the highest mark: ",highest_mark_name);

# 4. Find the student with the lowest marks.
lowest_mark = students["kamal"];
lowest_mark_name = "";

for name, mark in students.items():
    if lowest_mark >= mark:
        lowest_mark = mark;
        lowest_mark_name = name;

print("Lowest Mark: ", lowest_mark);
print("Name of the lowest mark: ",lowest_mark_name);

# 5. Calculate the average marks.
elements_count = len(students);
sum_of_values = 0;

for mark in students.values():
    sum_of_values = sum_of_values + mark;

average = sum_of_values / elements_count;
print("Average Mark: ", average);

# 6. Display students who scored more than 75 marks.
student_list = [];

for name,mark in students.items():
    if mark > 75:
        student_list.append(name);

print(student_list);

# 7. Allow the user to search for a student by name.
username = input("Search the user: ");
is_user_found = False;

for name, mark in students.items():
    if username == name:
        is_user_found = True;
        
if(is_user_found):
    print("User Found!");
else:
    print("User Unavilable!");