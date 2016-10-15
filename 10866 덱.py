def push_front(buf1, n):
    buf1.insert(0, n)
    return

def push_back(buf1, n):
    buf1.append(n)
    return

def pop_front(buf1):
    if buf1:
        print(buf1.pop(0))
    else:
        print(-1)
    return

def pop_back(buf1):
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

def front(buf1):
    if buf1:
        print(buf1[0])
    else:
        print(-1)
    return

def back(buf1):
    if buf1:
        print(buf1[-1])
    else:
        print(-1)
    return

n = int(input())
buf_list = []

for i in range(n):
    command = input().split()
    
    if command[0] == "push_front":
        push_front(buf_list, command[1])
    elif command[0] == "push_back":
        push_back(buf_list, command[1])
    elif command[0] == "pop_front":
        pop_front(buf_list)
    elif command[0] == "pop_back":
        pop_back(buf_list)
    elif command[0] == "size":
        size(buf_list)
    elif command[0] == "empty":
        empty(buf_list)
    elif command[0] == "front":
        front(buf_list)
    elif command[0] == "back":
        back(buf_list)
