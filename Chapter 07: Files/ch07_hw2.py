
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sum = 0.0
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sum = sum + float(line[20:])
    count = count + 1

print("Average spam confidence:", sum/count)
