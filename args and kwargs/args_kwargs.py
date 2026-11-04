# You can use both in the same function.
def display_details(*args, **kwargs):
    print("Positional Arguments:");

    for arg in args:
        print(arg);

    print("Keyword Arguments:")

    for key,value in kwargs.items():
        print(key, ":", value);

display_details(
    10, 
    "thenuka",
    city="Colombo",
    name="Kamal",
    age=25
)