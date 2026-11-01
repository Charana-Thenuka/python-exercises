# Create a dictionary containing 5 students and their marks. Display all student names and marks.
students = {
    "Kamal":75,
    "Nimal":80,
    "Vimal":85,
    "Amal": 95,
    "Saman": 80
}

marks = students.values();
items = students.keys();
print(items);

# Higest Mark
highest_mark = 0;

for x in marks:
    if(highest_mark < x):
        highest_mark = x;

print("Highest Mark: ",highest_mark)
