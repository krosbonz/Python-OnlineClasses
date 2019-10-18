fname = input("Enter file name: ")
fn = open(fname)
count = 0
for line in fn:
    if line.startswith('From '):
        stuff = line.split()
        count += 1
        print(stuff[1])

print("There were", count, "lines in the file with From as the first word")

