import sys

fh = sys.stdin
i = 0

for line in fh:
  i += 1

fh.close()
print(i)