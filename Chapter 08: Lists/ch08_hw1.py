fname = input('Enter file name: ')
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()

    words = line.split()

    for wds in words:
        if wds not in lst:
            lst.append(wds)
            lst.sort()
print(lst)

# # fhand = input('enter the file: ')
# fhand = open('romeo.txt')
# wds = list()
# for line in fhand:
#     linermv = line.rstrip() #remove the newline between each line
#     linesplit = linermv.split()
#     print('line', linesplit)
#     for wd in linesplit:
#         if wd not in wds:
#             wds.append(wd)
#     print("wd:", wds)
