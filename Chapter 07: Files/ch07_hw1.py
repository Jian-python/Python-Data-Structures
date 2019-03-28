print('Exercise 1: Write a program to read through a file and '
      'print the contents of the file (line by line) all in upper case.')
fname = open ('mbox.txt')
for line in fname:
    line = line.rstrip()
    print(line.upper())
