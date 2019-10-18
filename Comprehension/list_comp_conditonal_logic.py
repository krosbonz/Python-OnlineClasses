# List Comprehension with conditonal logic

nums = [1, 2, 5, 7, 8, 9, 14, 13]
 
evens = [num for num in nums if num % 2 == 0]
# For each num in nums if num mod 2 (if num/2 leaves remainder 0) 
# it's even
# odds = [num for num in nums if num % 2 =! 0]

[num*2 if num % 2 == 0 else num/2 for num in nums]
# if num in nums/2 has remainder of 0 multiply by 2
# else divide num by 2


vowels = "This is so much fun!"
''.join(char for char in vowels if char not in "aeiou")
# for each char in vowels if char not one of "aeiou" join the letters
# in a string with the "connector" empty string ''.

# Output
"Ths s s mch fn!"