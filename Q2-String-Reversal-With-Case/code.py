
# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

str = "Python is Awesome"
# print(str.lower())



def reverseStringCase(sentence):

    #to lower all the words
    lower_sentence = sentence.lower()

    individual_words = lower_sentence.split(" ")
    reversed_words = []
    print(individual_words)
    for word in individual_words:
        reversed_word = word[::-1]

        #to capitalize first letter of the words
        reversed_word = reversed_word[0].upper() + reversed_word[1:]
        
        print(reversed_word)
        reversed_words.append(reversed_word)
        new_sentence = " ".join(reversed_words)
    return new_sentence
    
lower_sentence = reverseStringCase(str)
print(lower_sentence)

