# 1.file hande as a sequence
handle = open('test.txt')
for cheese in handle:
    print(cheese)
# cheese means iteration variable, print out each line of file test.txt
print('#####################################################')
# 2.counting lines in a file
handle = open('test.txt')
count = 0
for line in handle:
    count = count+1
print('Line count:', count)
# 2.counting lines in a file
handle = open('mbox.txt')
count = 0
for line in handle:
    count = count+1
print('Line count:', count)
# "line" is just a random name of iteration variable!
print('#####################################################')
print('3.Reading the *whole* file')
print('you can red the whole file (newline and all) '
      'into a single string')
fhand = open('test.txt')
ghand = open('test.txt', 'r')
# you have to use string.read() to read whole thing into string,
# also read newline as "\n"
inp = fhand.read()
print(len(inp))  # print the length of the file
print(inp)
print('fhand is', fhand)
print('ghand is', ghand)
# means 'r' in open doesn't read the file
print(inp[:20])  # print out the first 20 letters
# (not included the 20th character!)
print('#####################################################')
# 4.Search through a file
print('put an "if" statement in "for" loop '
      'to only print out certain lines')
fhand = open('mbox_short.txt')
for line in fhand:
    if line.startswith('From: '):
        print(line)
# already checked, all lines meet the criteria are printed out
# Problem: lots of blank line between each line.
# Reason: 1. each line from the file has a "newline" at the end
#         2. "print" statement add "newline" to each line
#Solution: strip the whitespace from
# the right-hand side of the string using "rstrip()"
# newline is considered as whitespace
print('fixed version: strip newline:')
fhand = open('mbox_short.txt')
for line in fhand:
    if line.startswith('From: '):
        print(line.rstrip())
# or print('fixed version: strip newline:')
# fhand = open('mbox_short.txt')
# for line in fhand:
#     line = line.rstrip() <---------------------
#     if line.startswith('From: '):
#         print(line)
print('#####################################################')
print('4.skipping with continue')
print('we can conveniently skip a line by '
      'using "continue" statement')
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        continue
    print(line)
print('*******************')
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)
print('#####################################################')
print('5. Usnig "in" to select lines')
print('we can find a string in a line as our selection criteria')
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
print('**********************')
fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za')== -1:
        continue
    print(line)
    print(line.find('@uct.ac.za'))
    #'find' statement:  either returns the position of the string
    #  or -1 if the string was not found
print('#####################################################')
print('6.promp with file name')
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
subject = input('we gonna find: ')
count =0
for line in fhand:
    line = line.rstrip()
    if line.startswith(subject):
        count = count+1
print('there are', count, 'subject lines in', fname )
print('#####################################################')
