with open ("newfile.txt", "w+") as file:
    file.write("Te iubesc, Andreea\n")
    file.seek(0)
    data = file.read()
