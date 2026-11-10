# Find numbers greater than 50.

numbers = [25, 60, 45, 80, 35, 90, 55];
new_numbers = list(filter(lambda number : number > 50, numbers));

print(new_numbers);