# Use map() and lambda to create a new list containing the square of each number.

numbers = [2, 4, 6, 8, 10]
square = list(map(lambda number : number**2, numbers));

print(square);