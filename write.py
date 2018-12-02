#Append to a file
f = open('newfile.txt', 'a')
#Creating a list of strings
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
#Join lines separated by \n
text = '\n'.join(lines)
#Write lines to file
f.writelines(text)
f.close()