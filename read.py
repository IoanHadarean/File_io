#Opens relative_data.txt with an absolute path
f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')
#Reads through the lines as text(Note: readlines gets the lines as a list of strings)
lines = f.read()
#Closes the open file
f.close()
#Prints the lines
print(lines)