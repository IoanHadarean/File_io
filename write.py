#Write to a file
f = open('newfile.txt', 'w')
f.write("World")
#Append to a file
f = open('newfile.txt', 'a')
f.write("Hello")
f.close()