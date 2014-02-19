import string

with open("problem22.in", "r") as myfile:
        input_str = myfile.read()

#input_str = '''"A","C","B"'''
final_res = 1 * 1 + 2 * 2 + 3 * 3

retval = 0

input_str = sorted(input_str.split(","))

for word_index, word in enumerate(input_str):
    word = word[1:-1].lower()
    for letter in word:
        index = string.lowercase.index(letter) + 1
        retval += index * (word_index + 1)
print final_res, retval
