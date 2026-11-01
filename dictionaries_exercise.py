# Create a dictionary containing 5 students and their marks. Display all student names and marks.
students = {
    "Kamal":75,
    "Nimal":80,
    "Vimal":85,
    "Amal": 95,
    "Saman": 80
}

marks = students.values();

# Higest Mark
highest_mark = 0;
highest_name = "";

for name, marks in students.items():
    if(highest_mark < marks):
        highest_mark = marks;
        highest_name = name;

print("Highest Mark: ",highest_mark)
print("Name: ",highest_name);

# remove Duplicates from list
list = [10,20,30,10,52,10,20,58];
string_list = ["Kamal", "Nimal", "Vimal", "Kamal", "Vimal"];
unique_list = set(list);
string_unique_list = set(string_list);

print("Unique List: ", unique_list);
print("Unique String List: ", string_unique_list);



