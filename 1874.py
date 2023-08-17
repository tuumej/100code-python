import sys

N = int(sys.stdin.readline())
k = -1
oque = [x for x in range(N,0,-1)]
tque = []
yque = []

for i in range(N):
  m = int(sys.stdin.readline())
  if i==0:
    for _ in range(m):
      yque.append(oque.pop())
      tque.append('+')
    if yque.pop() == m:
      tque.append('-')
    else:
      break
    k = m
  else:
    if k>m:
      if yque.pop() == m:
        tque.append('-')
      else:
        break
    else:
      for _ in range(m-k):
        yque.append(oque.pop())
        tque.append('+')

      if yque.pop() == m:
        tque.append('-')
      else:
        break
    k = m

if len(tque) == 2*N:
  for i in tque:
   print(i)
else:
  print('NO')




