#!/usr/bin/python
import argparse
from graph import Graph
from node import Node
import sys
import fileinput
from util import helper
import time


#read arguments
parser = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
parser.add_argument("-o","--output", help="Output file to write solution")
parser.add_argument("-i","--infile", help="Input graph file. Graph must be in DIMACS format", type=argparse.FileType('r'))
args = parser.parse_args()

g = helper.readGraph(args)

#start = time.time()


#run algorithms and compute shortest paths
C = g.max_edge_length()

s = g.get_source()
k = 0

node_list = [[] for i in range(C+1)] #Circular list
node_list[0].append(s)

min_nodes = helper.find_min_dist(node_list, k) #retrieve first non-empty bucket
while(min_nodes != None):
    for node in min_nodes[1]:
        neighbors = g.neighbors(node)
        for nbs_j in neighbors:
            if (g.get(node).distance + nbs_j[1]) < g.get(nbs_j[0]).distance:
                prev_dist = g.get(nbs_j[0]).distance
                #update graph and node parent
                g.update_distance(nbs_j[0], g.get(node).distance + nbs_j[1])
                g.update_parent(nbs_j[0], node)

                #update the position in nodelist
                if prev_dist != float("inf"):
                    node_list[int(prev_dist) % (C+1)].remove(nbs_j[0])
                node_list[int(g.get(nbs_j[0]).distance) % (C+1)].append(nbs_j[0])
    node_list[k] = []
    k = min_nodes[0]
    min_nodes = helper.find_min_dist(node_list, k)
#end = time.time()
#print '%e' % (end - start)
helper.writeGraph(args, g)
