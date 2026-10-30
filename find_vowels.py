word = input("Enter a word: ");
lowercase_word = word.lower();
vowel_count = 0;

for letter in lowercase_word:
    if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        vowel_count = vowel_count + 1;

print("Number of vowels:",vowel_count);