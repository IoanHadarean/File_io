#Imports regular expressions and collections
import re
import collections

#Opens the book.text and reads everything as lowercases
text = open('book.txt').read().lower()
#Finds all the words that are not a white space(w) and that occur once or more(+)
words = re.findall('\w+', text)
#Prints the counter of the most common ten words that meet the requirements
print(collections.Counter(words).most_common(5))

