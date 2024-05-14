# Exercise Name:
# 	01-String-Reversal
# Description:
# 	Reverse each word of a string.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"nohtyP si emosewA"

str = "Pyhton is Awesome"

def reverseEachWord(sentence):

    #split the sentence into individual words
    individual_words = sentence.split(" ")

    #creating an empty array for storing reversed sentence
    reversed_string = []
    # print(individual_words)

    #for loop for taking each individual words
    for word in individual_words:

        #to reverse each word
        reversed_word = word[::-1]
        # print(reversed_word)

        #to append the reversed words into the empty array
        reversed_string.append(reversed_word)

        #to join the words using " "
        newSentence = " ".join(reversed_string)
        
    return newSentence

rev_string = reverseEachWord(str)
print(rev_string)