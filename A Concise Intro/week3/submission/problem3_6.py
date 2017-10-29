# -problem3_6.py *- coding: utf-8 -*-
import sys     # we need this library to deal with operating system

filein = sys.argv[1]
fileout = sys.argv[2]

infile = open(filein)
outfile = open(fileout,'w')
chctr = 0


for line in infile:
    chctr = chctr + len(line) -1
    chctr_ = str(chctr)
    outfile.write(chctr_+"\n")
    

infile.close()
outfile.close()

