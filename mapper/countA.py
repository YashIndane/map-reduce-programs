import sys

fh = sys.stdin

for line in fh:
   if line == 'A\n':
      line = line.strip()
      print(line)

fh.close()