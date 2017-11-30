name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hrtime = dict()

for line in handle:
    words = line.split()
    if not line.startswith('From '): continue
    else:
        for word in words:
            if ':' not in word: continue
            else:
                hrs = word.split(':')
                hrs_ = hrs[0]
                #print(hrs_)
                hrtime[hrs_] = hrtime.get(hrs_, 0) +1
for k,v in sorted(hrtime.items()):
    print(k,v)
