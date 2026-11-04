'''
    Create a calculator function.

    Create a function called calculate_total().

    Requirements:
    - Accept any number of numerical arguments using *args.
    - Calculate their total using a for loop.
    - Return the total.
    - Call the function with different numbers of arguments.
'''

def calculate_total(*args):
    total = 0;
    for arg in args:
        total += arg;

    return total;

sum = calculate_total(10,20,5,74,8);
print(sum);

'''
    Create an employee details function.

    Create a function called employee_details().

    Requirements:
    - Accept employee details using **kwargs.
    - Display all keys and values using a for loop.
    - Pass name, age, department, and salary when calling the function.
'''

def employee_details(**kwargs):
    for key,value in kwargs.items():
        print(key, ":", value);

employee_details(
    name="thenuka",
    age=25,
    department="IT",
    salary=70000
)

'''
    Create a function called student_information().

    Requirements:
    - Accept subjects using *args.
    - Accept student information using **kwargs.
    - Display all subjects.
    - Display all student information.
'''

def student_information(*args, **kwargs):
    # display subjects
    for subject in args:
        print(subject);

    # diaplay all student informatins
    for key,value in kwargs.items():
        print(key, ":", value);

student_information(
    "Python",
    "Java",
    "IOT",
    name="Sewwandi",
    student_id = "IT-2110-0110",
    department = "IT"
)