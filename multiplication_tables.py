number = int(input("Enter a Number: "));
ending_number = int(input("Enter ending number: "));
iterate_count = ending_number + 1;

print(ending_number);

for x in range(1, iterate_count):
    print(number, "x", x, "=", (number*x));