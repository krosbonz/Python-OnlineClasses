
namefile = input('Enter a file name: ')
fileopen = open(namefile)

email = dict()
for line in fileopen:
    words = line.split()
    if not line.startswith('From: ') : continue
    else:
        for word in words:
            if '@' in word:
                email[word] = email.get(word,0) + 1

bigword = None
bigcount = None
for k,v in email.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v

print(bigword, bigcount)