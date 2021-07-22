fname = input('enter the name:')
fhand = open(fname)
counts = dict()
for lines in fhand:
    lines = lines.strip()
    if lines == '':
        continue
    value = lines.split()
    if value[0] != 'From':
        continue
    words = value[1]
    counts[words] = counts.get(words, 0)+1
    print(counts)
bigcount = None
bigword = None
for count, word in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
