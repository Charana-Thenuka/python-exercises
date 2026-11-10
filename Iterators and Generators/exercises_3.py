def countdown(start):
    for count in range(start):
        yield (start - count);

results = countdown(5);

for number in results:
    print(number);
