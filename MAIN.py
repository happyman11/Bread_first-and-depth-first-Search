#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:00:23 2021

@author: ravishekhartiwari
@website: https://www.rstiwari.com
"""
import FUNCTIONS as funct

if __name__ == '__main__':
    
    graph_bfs = {0: [1, 2], 
                 1: [2], 
                 2: [3], 
                 3: [1, 2]}
    
    graph_dfs = {"A":["B","C", "D"],
                 "B":["E"],
                 "C":["F","G"],
                 "D":["H"],
                 "E":["I"],
                 "F":["J"]}
    print("Breadth First Traversal: ")
    Starting_Node=0
    funct.bfs(graph_bfs, Starting_Node)
    
    print("Depth First Traversal: ")
    Start="A"
    path = funct.recursive_dfs(graph_dfs, Start)
    print(" ".join(path))
    
    
    