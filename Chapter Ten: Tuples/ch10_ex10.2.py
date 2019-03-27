counts = dict()
lst = list()
hour = list()
fhand = open('mbox_short.txt')
for line in fhand:
    words = line.split()
    if len(words)>3 and words[0] == 'From':
        lst.append(words[5])
for time in lst:
    timesp = time.split(':')
    hour.append(timesp[0])
for hr in hour:
    counts[hr] = counts.get(hr, 0) + 1
store = list()
for key, val in counts.items():
    newtup = (key, val)
    store. append(newtup)
store = sorted(store)
for key, val in store:
    print(key, val)
