from graph import Graph, Vertex
from collections import deque
import random

def dfs(start, end, graph):
    stack = []
    start_vertex = graph[start]
    stack.append(start_vertex)
    start_vertex.visited = True
    while len(stack) > 0:
        top = stack[len(stack)-1]
        if top.label == end:
            return stack
        else:
            unvisited = []
            for neighbor in top.neighbors:
                if not neighbor.visited:
                    unvisited.append(neighbor)
            if len(unvisited) > 0 :
                neighbor = random.sample(unvisited, 1)[0]
                neighbor.visited = True
                stack.append(neighbor)
            else:
                stack.pop()
    return []

def bfs(start, end, graph):
    queue = deque()
    start_vertex = graph[start]
    queue.append([start_vertex])
    start_vertex.visited = True
    while len(queue) > 0:
        first_search = queue[0]
        top_vertex = first_search[len(first_search)-1]
        if top_vertex.label == end:
            return first_search
        else:
            unvisited = []
            for neighbor in top_vertex.neighbors:
                if not neighbor.visited:
                    unvisited.append(neighbor)
            if len(unvisited) > 0 :
                neighbor = random.sample(unvisited, 1)[0]
                neighbor.visited = True
                new_search = first_search.copy()
                new_search.append(neighbor)
                queue.append(new_search)
            else:
                queue.popleft()
    return []
