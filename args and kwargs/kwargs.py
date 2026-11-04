# syntax - **kwargs
# store the values into dictonary

# Difference between *args and **kwargs

'''
    Feature	        *args	                **kwargs
    Accepts	        Positional arguments    Keyword arguments
    Stores data as	Tuple	                Dictionary
    Example	        10, 20, 30	            name="Kamal"
    Access	        for x in args	        for k, v in kwargs.items()
'''

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value);
    print(type(kwargs));

student_details(
    name = "Thenuka",
    age = 25,
    location = "Piliyandala",
    is_married = False
)