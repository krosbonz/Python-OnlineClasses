def problem3_1(txtfilename):
    infile = open(txtfilename)
    charct = 0
    for line in infile:
        charct = charct + len(line)
        print(line, end="")  
        
    infile.close()
    print()    
    print()
    print("There are", charct, "letters in the file.")