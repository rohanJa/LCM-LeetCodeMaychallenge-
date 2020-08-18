import heapq    

l=[12,3,56,32,7]

heapq.heapify(l)
print(l)
for i in range(0,len(l)):
    print(heapq.heappop(l))

print('{:.2f}'.format(12345.4567))