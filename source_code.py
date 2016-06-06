#An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:
# "board": makes "bad" and "or".
#  "waists": makes "wit" and "ass".
#
#
#Using the word list at unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion.

#max_leng_of_word = 14

with open("unixdict.txt", "r") as f:
    words = f.readlines()
f.closed

words = [s.strip("\n") for s in words]

#creating a dict with a member after each word which contains an empty list

potential_words = {str(word): ["evennumberword", "oddnumberword"] for word in words}

#adding to the dict member of each word it's even number and odd number chars made words, in total: 2 words as 

for word in words:
    even_number_word = ""
    odd_number_word = ""
    try:
        for i in range(14):
            if i % 2 == 0:
                even_number_word = "".join([even_number_word, word[i]])
            elif not i % 2 == 0:
                odd_number_word = "".join([odd_number_word, word[i]])
    except IndexError:
        potential_words[str(word)][0] = even_number_word
        potential_words[str(word)][0] = odd_number_word
        print(word, "evennumber is", even_number_word, "and oddnumber is", odd_number_word)
    if even_number_word in set(words) and odd_number_word in set(words):
        print(word, "is an alternade")
    else:
        print(word, "is not an alternade")
#didn't take out dict creation part cause it might be used to write this info in another file
