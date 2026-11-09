def calculate_total(*args):
    sum = 0;
    for arg in args:
        sum = sum + arg
    return sum;

sum = calculate_total(10,20,30);
print("Addition is: ", sum);

def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key," : ", value);

employee_details(
    name="Thenuka",
    age=26,
    department="IT",
    salary=20000
)

def student_information(*args, **kwargs):
    # display all  subjects
    for arg in args:
        print(arg);

    # display all student informations
    for key,value in kwargs.items():
        print(key,":",value);

student_information(
    "maths","science","art",
    name="Anjalika",
    age=25,
    city="Kalubowila"
)