fname = input('Enter file:')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount, bigword = None, None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount, bigword = count, word

print(bigword, bigcount)
