#Prompt for file, find lines with specific information, for all files with spec info get average and print
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
tot = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        atpos = line.find("X-DSPAM-Confidence:")
        sppos = line.find(' ',atpos)
        place = line[sppos + 1:]
        tot = tot + float(place)
        count = count + 1
    
print("Average spam confidence:", tot/count)