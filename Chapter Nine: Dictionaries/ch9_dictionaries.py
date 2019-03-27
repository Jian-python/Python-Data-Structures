print('chapter 9 dictionaries')
print('***********part 1***********')
# collections include 'List' and 'Dictionary'
print('"List": a linear collection of values that stay in order')
print('"Dictionary": A "bag" of values, each with its own label, mess up with order!')
print('#####################################################')
print('1. Dictionaries')
# a dictionary as a mapping between a set of indices (which are called keys) and a set of values.
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])
print('you can change the value of the item (index-value pair) in dictionary')
purse['candy'] = purse['candy'] + 2
print(purse['candy'])
print('#####################################################')
print('***********part 2***********')
print('2. Dictionry literals')
# empty dictionary:{} ; dictionary lierals use curly braces and have a list of key:value pairs
empty = {}
print(empty)
print('#####################################################')
print('3. dictionary as a set of counters')
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] +1
print(d)
print('#####################################################')
print('4. Dictionary traceback')
# use key name in dictionary to check
name = dict()
while True:
    ip = input("enter name: ")
    if ip != 'none':
        if ip in name:
            name[ip] = name[ip] + 1
        else:
             name[ip] = 1

    else:
        print("total:", name)
        exit()
print('#####################################################')
print('5. the "get" method fro dictionary')
# if the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value
name = dict()
while True:
    ip = input("enter name: ")
    if ip != 'none':
            name[ip] = name.get(ip, 0) + 1
    else:
        print("total:", name)
        exit()

# really nice way to check the words in a file: we use romeo.txt here
wd =dict()
fhand = input("enter the file name: ")
line = open(fhand)
for i in line:
    i = i.rstrip()
    i = i.split()
    for o in i:
        wd[o] = wd.get(o, 0) +1
print(wd)
# nice!
print('REALLY ELEGANT!!!!!!')
print('***********part 3***********')
print("6. Dictionaries and files")
print('counting pattern for words in line: '
      'split the line into words, and loop through the wrods and use a dictionary'
      'to track the count of each word independently')
print('retrieving list of "keys()", "Values()", and "items()" ')

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
print(counts.keys(), '\n', counts.values(),'\n', counts.items(), sep='')
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
print('#####################################################')
print('6. Bonous: two iteration variables')
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for k, v in counts.items():
    print(k, v)
# we can better our code to select the bigword:
wd =dict()
fhand = input("enter the file name: ")
line = open(fhand)
for i in line:
    i = i.rstrip()
    i= i.split()
    for o in i:
        wd[o] = wd.get(o, 0) +1
bigk = None
bigv = None
for k,v in wd.items():
    if bigv is None or v > bigv:
        bigk = o
        bigv = v
print(bigk, bigv)
print('#####################nice!############################')

