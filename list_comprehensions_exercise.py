# 1. Create a list containing the squares of numbers from 1 to 10.
squre_numbers = [x*x for x in range(1,11)];
print(squre_numbers);

# 2. Create a list containing even numbers between 1 and 20.
even_numbers = [x for x in range(1,21) if x % 2 == 0];
print(even_numbers);

# 3. Given marks = [35, 75, 45, 90, 60, 25], create a new list containing only marks greater than or 
# equal to 50.
marks = [35, 75, 45, 90, 60, 25, 50];
new_marks = [x for x in marks if x >= 50];
print(new_marks);

# 4. Given names = ['kamal', 'nimal', 'amal'], create a new list with all names in uppercase.
names = ['kamal', 'nimal', 'amal'];
uppercase_names = [name.upper() for name in names];
print(uppercase_names);

# 5. Given words = ['Python', 'Django', 'Wagtail'], create a list containing the length of each word.
words = ['Python', 'Django', 'Wagtail'];
length_of_words = [len(word) for word in words];
print(length_of_words);