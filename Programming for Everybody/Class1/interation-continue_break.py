while True :
    line = input('> ')
    # if first character equals "#" "continue" brings you back to the beginning of while loop
    if line[0] == '#':
        continue
    # if input is "done" the loop will break out of the entire "while" block and print "Done!"
    if line == 'done':
        break
    print(line)
print("Done!")
