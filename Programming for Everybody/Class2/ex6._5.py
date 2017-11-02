text = "X-DSPAM-Confidence:    0.8475"

strnum = int(text.find('    '))

floatnum = float(text[pos:pos+10])

print(floatnum)
