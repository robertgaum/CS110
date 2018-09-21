#First, I create a variable called 'Phrase'
Phrase = ('The quick brown fox jumps over the lazy dog')

#then, I create a variable that defines the phrase but in all upper and lower case, and capitalize the first letter of every word
Phrase2 = Phrase.upper()
Phrase3 = Phrase.lower()
Phrase4 = Phrase.title()
#Next, I print those variables
print (Phrase2)
print (Phrase3)
print (Phrase4)

#Thirdly, I use the split method to turn each word in the sentence into a list
List = Phrase.split()
print (List)

#lastly, I use the join method to join back the list back into a sentence, but this time it has commas instead of spaces.
Phrase5 = ','.join(List)
print (Phrase5) 
