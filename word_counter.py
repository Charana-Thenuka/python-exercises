# get sentence form the user
sentence = input("Enter your sentence: ");

# convert the senetence into list
words_list = sentence.split();

# create empty dictorary to store the words and their counts
word_counter = {};

# store the values and keys inside the dictonary
for word in words_list:
    if word in word_counter:
        word_counter[word] += 1;
    else:
        word_counter[word] = 1;

# print the dictonary
print(word_counter);