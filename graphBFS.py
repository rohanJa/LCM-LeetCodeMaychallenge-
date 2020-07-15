graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []
queue.append('A')
visited.append('A')
while queue:

    s=queue.pop(0)
    
    for vertex in graph[s]:
        if vertex not in visited:
            queue.append(vertex)
            visited.append(vertex)
print(visited)