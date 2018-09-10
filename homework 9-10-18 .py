phrase = 'the quick brown fox jumps over the lazy dog'
#capitalise all characters in phrase
print (phrase.upper())
#make all lower case
print (phrase.lower())
#capitalise the first letter in each word
print (phrase.title())
#replace all o's with x's
print (phrase.replace('o','x'))
#split the phrase and print each word with a comma
splitphrase = phrase.split()
print (",".join(splitphrase))