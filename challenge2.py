#Opens love.txt in read + write mode
#Overwrites the first line of the file(cursor is at location 0)
#We store the current position in a variable, then we skip over line 2
#Our cursor is at the beginning of line 3
#We overwrite the third line
#We use f.seek(offset, from_where)
#from_where is: 0 (default) offset from the beginning of the file; 
#1 offset from the cursor pointer or
#2 offset from the end of the file.

with open("love.txt", "r+") as f:
    f.write("Andreiuta")
    curr_pos = f.tell()
    f.seek(curr_pos + 11)
    f.write("Andreiuta")
    f.seek(2, 2)
    f.write("\nCu drag, Ionica")