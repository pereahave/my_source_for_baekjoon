import heapq

def heapSort(lst):
    alst = []
    for v in lst:
        heapq.heappush(alst, v)
    return [heapq.heappop(alst) for i in range(len(alst))]

a = int(input())
input_list = []

for i in range(a):
    b = int(input())
    input_list.append(b)

heapSort(input_list)

for i in input_list:
    print(i)
