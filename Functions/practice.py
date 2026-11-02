# Exercise 1

""""
    Create a function called calculate_salary().

    Requirements:
    - Accept basic_salary.
    - Accept bonus, with a default value of 5000.
    - Calculate the total salary.
    - Return the total salary.
    - Call the function twice: once without providing a bonus and once with a custom bonus.
"""

def calculate_salary(basic_salary, bonus=5000):
    return basic_salary + bonus;

without_bonus = calculate_salary(50000);
with_bonus = calculate_salary(
    bonus=10000,
    basic_salary=50000
)

print("Without Bonus: ", without_bonus);
print("With Bonus: ", with_bonus);

# Exercise 2

"""
    Create a function called display_student().

    Requirements:
    - Accept name, age, and course.
    - Display all three values.
    - Call the function using keyword arguments in a different order.
"""

def display_student(name, age, course):
    print(name);
    print(age);
    print(course);

display_student(
    age=52,
    course="JavaSript",
    name="Charana"
)
