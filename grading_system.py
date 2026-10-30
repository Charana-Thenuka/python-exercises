# 90 - 100 → A+
# 80 - 89  → A
# 70 - 79  → B
# 60 - 69  → C
# 50 - 59  → S
# 0 - 49   → F

def grade_calculation(mark):

    if(mark >= 90 and mark <= 100):
        return "A+";
    elif(mark >= 80 and mark <= 89):
        return "A";
    elif(mark >= 70 and mark <= 79):
        return "B";
    elif(mark >= 60 and mark <= 69):
        return "C";
    elif(mark >= 50 and mark <= 59):
        return "S"
    elif(mark >= 0 and mark <= 49):
        return "F"

name = input("Enter student name: ");
mark = int(input("Enter marks: "));

print("Student: "+name);
print("Marks: ",mark);
print("Grade: "+ grade_calculation(mark));