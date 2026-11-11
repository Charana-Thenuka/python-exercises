'''
    Concepts: Variables, input, conditions, loops, lists, dictionaries, functions.

    Requirements:
    1. Create a dictionary containing five students and their marks.
    2. Display all student names and marks.
    3. Find the highest and lowest marks.
    4. Calculate the average mark.
    5. Display students who passed (marks 50 or above).
    6. Search for a student by name.
    7. Create a function to calculate a student's grade.
'''

students = {
    "Kamal" : 80,
    "Nimal" : 90,
    "Vimal" : 50,
    "Anil" : 60,
    "Sunil" : 85
}

for student in students.values():
    print(student);

lenght = len(students);
sum = 0;

# Average Mark
for average in students.values():
    sum = sum + average;

average = sum / lenght;
print("Average is: ", average);

passed_students = [];
for passed in students.values():
    if (passed >= 50):
        passed_students.append(passed);

print(passed_students);

# search the students by name
search = input("search student: ");

for search_student in students.keys():
    if (search == search_student):
        print(f"{search}, is available");





