# ###################beter version:##########################

# fhand = input('enter the file: ')
fhand = open('mbox_short.txt')
email = list()
count = 0
for line in fhand:
    linermv = line.rstrip() # type:str
    linesplit = linermv.split() # type:list
    if len(linesplit) > 3 and linesplit[0] == 'From':
        print(linesplit[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')

# don't use str.startswith('From'), because it will select both From and From:


# fname = input('Enter a file name: ')
# fh = open(fname)
# lst = list()
# count = 0
# for i in fh:
#     if i.startswith('From'):
#         i.rstrip()
#         words = i.split()
#         # if i.startswith('From: '): continue
#         if words[0] != 'From' : continue
#         count = count + 1
#     print(words[1])
# print('There were', count, 'lines in the file with From as the first word')


