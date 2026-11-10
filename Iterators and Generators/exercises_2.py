'''
1. Create a generator function called even_numbers().
    - Generate even numbers from 2 to 10 using yield.
    - Call the function.
    - Display all generated numbers using a for loop.
'''

def even_numbers():
    yield 2;
    yield 4;
    yield 6;
    yield 8;
    yield 10;

results = even_numbers();
print(next(results));

for even_number in results:
    print(even_number)
