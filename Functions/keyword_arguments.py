# Normally, you pass arguments according to their position. But you can also specify the parameter names.
# Notice that the order doesn't matter when you use keyword arguments.

# normal function with calling same parameters by same positions
def my_function(name, age, course):
    print("My name is:", name);
    print("My age is:", age);
    print("My course name is:", course);

my_function("Thenuka", 25, "Python");

# Function with Keyword Arguments
def keyword_arguments(name, age, course):
    print("My name is:", name);
    print("My age is:", age);
    print("My course name is:", course);

keyword_arguments(
    age=26,
    name="Anjalika",
    course="Human Resource"
)