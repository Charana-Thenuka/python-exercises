number_list = [];
largest_number = 0;
smallest_number = 0;
total = 0;
average = 0;

for x in range(1,6):
    number_list.append(int(input("Enter number "+ str(x) + ": ")));

print(number_list);

# Find Largest Number
largest_number = number_list[0];

# Find Smallest Number
smallest_number = number_list[0];

for x in range(5):
    # Find Largest Number
    if(largest_number <= number_list[x]):
        largest_number = number_list[x];

    # Find Smallest Number
    if(smallest_number >= number_list[x]):
        smallest_number = number_list[x];

    # calculate total
    total += number_list[x];

print("Largest number:",largest_number);
print("Smallest number:",smallest_number);
print("Total: ",total);
print("Average: ", int((total/len(number_list))));
