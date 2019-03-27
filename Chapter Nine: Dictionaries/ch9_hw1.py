import pprint
wd = dict()
fhand = input("enter the file name: ")
line = open(fhand)
for i in line:
    i = i.rstrip()
    i= i.split()
    if len(i) >3 and i[0] == 'From':
        wd[i[1]] = wd.get(i[1], 0) + 1

pprint.pprint(wd)
bigk = None
bigv = None
for k,v in wd.items():
    if bigv is None or v > bigv:
        bigk = k
        bigv = v
print(bigk, bigv)