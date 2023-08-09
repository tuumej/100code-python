# zero
import sys

def fn_10773():
  n = int(sys.stdin.readline())
  ll = []
  
  for _ in range(n):
    tt = int(sys.stdin.readline())
    if tt:
      ll.append(tt)
    else:
      ll.pop()
  
  print(sum(ll))

if __name__ == "__main__":
  function = fn_10773
  function()

