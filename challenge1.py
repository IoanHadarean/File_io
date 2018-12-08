with open ("newfile.txt", "w+") as f:
    f.write("Te iubesc, Andreea\n")
    f.seek(0)
    lines= f.read()
