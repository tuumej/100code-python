import sys
N = int(sys.stdin.readline())

stack = []

for i in range(N):
    tmp = sys.stdin.readline().split()
    if len(tmp) > 1:
        stack.append(int(tmp[1]))
    elif tmp[0] == 'pop':
        print(stack.pop()) if len(stack) > 0 else print(-1)
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        print(1 if len(stack) == 0 else 0) 
    elif tmp[0] == 'top':
        print(stack[-1])
    
