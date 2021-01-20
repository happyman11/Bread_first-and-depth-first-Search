#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:56:41 2021

@author: ravishekhartiwari
"""

def bfs(graph, root):
    import sys
    import collections

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def recursive_dfs(graph, source,path = []):

       if source not in path:

           path.append(source)

           if source not in graph:
               # leaf node, backtrack
               return path

           for neighbour in graph[source]:

               path = recursive_dfs(graph, neighbour, path)


       return path
