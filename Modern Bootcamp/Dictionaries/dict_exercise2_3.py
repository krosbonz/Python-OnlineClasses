
# Excercise 2
# Create a dict with key as a vowel and 0 as the value. End result should be
{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# My answer
answer = {}.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)

# Also could have used...

# Using a dictionary comprehension:
answer = {char:0 for char in 'aeiou'} 

# Using dict.fromkeys:
answer = dict.fromkeys("aeiou", 0) 



# Exercise 3
# Create a dictionary that maps ASCII keys to their corresponding letters. 
# Only worry about capital A > Z

# Option 1
import string

letter = string.ascii_uppercase
asc_cnt = []

for i in range(65, 100):
    asc_cnt.append(f"chr({i})")

answer = {letter[x]:asc_cnt[x] for x in range(0, len(letter))}
print(answer)

# Option 2

letter = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
asc_cnt = []

for i in range(65, 100):
    asc_cnt.append(f"chr({i})")

answer = {letter[x]:asc_cnt[x] for x in range(0, len(letter))}
print(answer)