def push(buf1, n):
    buf1.append(n)
    return

def pop(buf1):
    if buf1:
        print(buf1.pop(-1))
    else:
        print(-1)
    return

def size(buf1):
    print(len(buf1))
    return

def empty(buf1):
    if not buf1:
        print(1)
    else:
        print(0)
    return

def top(buf1):
    if buf1:
        print(buf1[-1])
    else:
        print(-1)
    return

n = int(input())
buf_list = []

for i in range(n):
    command = input().split()
    
    if command[0] == "push":
        push(buf_list, command[1])
    elif command[0] == "pop":
        pop(buf_list)
    elif command[0] == "size":
        size(buf_list)
    elif command[0] == "empty":
        empty(buf_list)
    elif command[0] == "top":
        top(buf_list)
