fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.strip()
    if line.startswith('From'):
        continue
    if not line.startswith('From:'):
        continue
    value=line.split()
    print(value[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
rhg23fjrgfkugygwtjhgjhgghbhlirgilroughgwoguhgtj,nghire