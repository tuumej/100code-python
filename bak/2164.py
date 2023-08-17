import sys
sys.setrecursionlimit(10**7)

ll = [x+1 for x in range(int(input()))]

def solv():
  if len(ll) < 2:
    print(ll[0])
  else:
    ll.pop(0)
    ll.append(ll.pop(0))
    solv()

solv()

  

