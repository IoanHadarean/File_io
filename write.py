#Append to a file
f = open('newfile.txt', 'a')
#Creating a list of strings
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
#Write lines to file
f.writelines(lines)
f.close()