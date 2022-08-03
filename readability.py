#Developed by Karinne Vieira
#This code calcules the readability index (from 1 to 14) of an English sentence.
import math

sentence = input('Type one phrase in english:')

def automated_readability_index(sentence):
    #number of words
    words = sentence.split(' ')
    num_words = len(words)

    #number of letters
    num_letters = 0
    for i in range(len(words)):
        count = len(words[i])
        num_letters = num_letters + count
    
    #number of phrases
    num_phrases = 1

    #readability evaluation
    readability = math.ceil((4.71*(num_letters/num_words))+(0.5*(num_words/num_phrases))-21.43)

    #function output
    if readability > 14:
        return (14)
    elif readability <1:
        return (1)
    else:
        return (readability)

print(automated_readability_index(sentence))

