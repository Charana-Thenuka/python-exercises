'''
    3. What is a generator?
        A generator is a special type of iterator that produces values one at a time instead of storing all the values in memory at once.

        You create a generator using a function with the yield keyword.

        Compare return and yield:
        - return sends a result back and finishes the function.
        - yield sends a result back but pauses the function, allowing it to continue later.
'''

def count_numbers():
    yield 1;
    yield 2;
    yield 3;

result = count_numbers();

print(next(result)); # print 1
print(next(result)); # print 2
print(next(result)); # print 3