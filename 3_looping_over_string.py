# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
word= input("Write your chosen word:")
print(word)

for letters in word:
    list1= [letters]
    print(list1)

vowels= "aeiouAEIOU"
count=0
# Challenge:
# Count how many vowels are in the word.

for letters in word:
    if letters in vowels:
        count+= 1
print("Vowels: ", count)