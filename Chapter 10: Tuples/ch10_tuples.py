print('chapter 10 Tuples')
print('***********part 1***********')
print('1. Tuples are immutable, tuples are like lists')
# tuples are another kind of sequence that functions much like a list
# For a temporary variable that you will use and discard without modifying
# they have elements whixh are indexed starting at 0
#  a tuple is a comma-separated list of values, enclose tuples in parentheses
x = ('Glenn', 'Sally', 'Joseph')
print(type(x))
# <class 'tuple'>
y = (1, 9, 2)
print(type(y))
# <class 'tuple'>
z = ['Joe', 'Glenn', 'Sally']
print(type(z))
# <class 'list'>
# immutable: tuple(), string''
# mutable: list[]
print('list:mutable')
x = [9, 8, 7]
x[1] = 10
print(x)
print('#####################################################')
print('2. things not to do with tuples:')
print('.sort, .append, .reverse')
print('#####################################################')
print('3. a tale of two sequence:')
l = list()
print('list:', dir(l)[35:])
t = tuple()
print('tuple:', dir(t)[31:])
print('tuple are simpler and more efficient'
      'so we prefer tuples over list when making "temporary variable"')
print('#####################################################')
print('tuple and assignment')
# we can put a tuple on the left-hand side of a assignment statement
# we can even omit(ignore) the ()
(x, y) = (4, 'fred')
(a, b) = (99, 98)
print(x)
print(a)
print('tuples amd dictionaries')
print('the items() method in dictionaries returns a list of (key, value) tuples')
d =dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print('d.items():', k,v)
tups = d.items()
print('tuples:', tups)
print('#####################################################')
print('tuple are comparable')
# Python starts by comparing the first element from each sequence.
# If they are equal, it goes on to the next element, and so on, until it finds elements that differ.
print((0, 1, 2000000) < (0, 3, 4))
print(('Adam', 'lee') > ('Zoe', 'lee'))
print('Adam' > 'zoe') # we can even omit(ignore) the ()
print('adam' > 'Zoe')
print('use sorted() to sort a list of tuples to get sorted version of dictionary')
# to sort a dictionary by the key using the items() method and sorted() function
d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
t = sorted(d.items())
print(t)
print('loop the dictionary in key order')
d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
t = sorted(d.items())
# watch out: t:type(t) <class 'list'>, cannot use items()
for k, v in sorted(d.items()):
    print(k, v)
print('loop the dictionary in value order')
# construct a list of tuples of form (value, key) so we can sort value
print('********************sorted********************')
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp.sort(reverse=True)
print('sort tmp:', tmp)
print('********************sorted********************')
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print('sorted tmp:', tmp)
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数
# sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作
print('#####################################################')
print('the top 10 must commmon words')
print('********************sort********************')
counts = dict()
fhand = open('romeo.txt')
for line in fhand:
    words= line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)
for val, key in lst[:10]: # val, key flipped out!!!!!
    print(key, val)
print('********************sorted********************')
counts = dict()
fhand = open('romeo.txt')
for line in fhand:
    words= line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
# begin=============================
# this part can be shorten
for key, val in counts.items():
    newtup = (val, key)
    lst. append(newtup)
lst = sorted(lst, reverse=True)
# end=============================
for val, key in lst[:10]:
    print(key, val)
print('********************Even shorter version********************')
# "List Comprehension" creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
# begin=============================
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()], reverse=True))
# end=============================
print('summary: immutability, comparability, sorting, tuples in assignment statements, sorting dictionaries by either key or value')
