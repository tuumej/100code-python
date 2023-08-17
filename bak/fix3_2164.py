import sys

N = int(sys.stdin.readline())

i = 1

while N>i:
  i*=2

if N==i:
  print(i)
else:
  print(2*N-i)
