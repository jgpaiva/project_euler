limit = 100

all_entries = set()
for i in xrange(2, limit + 1):
    for j in xrange(2, limit + 1):
        all_entries.add(i ** j)
print len(sorted(all_entries))
