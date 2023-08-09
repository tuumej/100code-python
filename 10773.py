# zero
import sys

N = int(sys.stdin.readline())
ll = []

for i in range(N):
  tt = int(sys.stdin.readline())
  if tt < 1:
    ll.pop()
  else:
    ll.append(tt)

print(sum(ll))
