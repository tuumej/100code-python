import sys

def binary_search(ll, tt, ss, ee):
  if ss  > ee:
    return 0 

  mid = (ss + ee) // 2

  if ll[mid] == tt:
    return 1 
  elif ll[mid] < tt:
    return binary_search(ll, tt, mid+1, ee)
  elif ll[mid] > tt:
    return binary_search(ll, tt, ss, mid-1)

N = int(sys.stdin.readline())
ll = list(map(int,sys.stdin.readline().split()))
ll.sort()

M = int(sys.stdin.readline())
tt = list(map(int,sys.stdin.readline().split()))

for i in range(M):
  print(binary_search(ll, tt[i], 0, M-1))
