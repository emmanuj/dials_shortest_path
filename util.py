from graph import Graph
from node import Node

class helper:
    def __init__(self):
        pass
    #loops through the circular list of buckets and returns the first non-empty
    @staticmethod
    def find_min_dist(lst, k):
        for i in range(0,len(lst)):
            if(len(lst[(k+i)% len(lst)])) >0:
                return [(k+i)% len(lst), lst[(k+i) % len(lst)]]
        return None

    #convenient function for creating the graph from file
    @staticmethod
    def readGraph(args):
        g = None
        #read in graph
        if(args.infile != None):
            for line in args.infile:
                if line[0] == "p": #process p records
                    l = line.split(" ")
                    if not l[2].strip() or int(l[2].strip())==0:
                        print "Error: # of nodes is either 0 or not specified"
                        exit(1)
                    g = Graph(int(l[2].strip()))
                #create edges
                if line[0] == "a": #process a records
                    if g.size() > 0:
                        l = line.split(" ")
                        u = int(l[1].strip())
                        v = int(l[2].strip())
                        w = int(l[5].strip())
                        #do csome trivial error checking
                        if u == v:
                            print "Error: Self loop edges not supported"
                            exit(1)
                        if w < 0:
                            print "Error: Negative edge weights not supported"
                            exit(1)
                        g.add_edge(u-1,v-1,w) #add edge to graph
                    else:
                        print "Error: Can't add edge to empty graph"
                        exit(1)
                if line[0] == "n": #process n records
                    l = line.split(" ")
                    if int(l[2].strip()) == 1:
                        g.set_source(int(l[1].strip()) - 1)
        else:
            print "First enter p record e.g p min 10 15 \n then enter edge line by line in the format a u v x y w \n next enter the n records e.g n 1 1\n Press enter each time. \nPress enter twice when done."
            line = raw_input("==> ")
            while line !="":
                #create edges
                if line[0] == "p": #process p records
                    l = line.split(" ")
                    if not l[2].strip() or int(l[2].strip())==0:
                        print "Error: # of nodes is either 0 or not specified"
                        exit(1)
                    g = Graph(int(l[2].strip()))
                #create edges
                if line[0] == "a": #process a records
                    if g.size() > 0:
                        l = line.split(" ")
                        u = int(l[1].strip())
                        v = int(l[2].strip())
                        w = int(l[5].strip())
                        #do csome trivial error checking
                        if u == v:
                            print "Error: Self loop edges not supported"
                            exit(1)
                        if w < 0:
                            print "Error: Negative edge weights not supported"
                            exit(1)
                        g.add_edge(u-1,v-1,w) #add edge to graph
                    else:
                        print "Error: Can't add edge to empty graph"
                        exit(1)
                if line[0] == "n": #process n records
                    l = line.split(" ")
                    if int(l[2].strip()) == 1:
                        g.set_source(int(l[1].strip()) - 1)
                line = raw_input("==> ")

        return g

    #write output to file
    @staticmethod
    def writeGraph(args, g):
        edges = {}
        for i in range(0, g.size()):
            node = g.get(i)
            while node.parent != node:
                edge = ( node.parent.id, node.id)
                if edge in edges:
                    edges[edge] = edges[edge] + 1
                else:
                    edges[edge] = 1
                node = node.parent

        if(args.output != None):
            with open(args.output,"w") as f:
                soln =0
                for m in edges:
                    f.write("f "+ str(m[0] -1)+" "+str(m[1]-1)+" "+str(edges[m])+"\n")
                    soln= soln + ( edges[m] * g.find_arc_length(m[0],m[1]))
                f.write("s "+str(soln)+"\n")
                f.flush()
        else: #no output file. Write to stdout
            soln =0
            for m in edges:
                print "f", m[0] -1,m[1]-1,edges[m]
                soln= soln + ( edges[m] * g.find_arc_length(m[0],m[1]))
            print "s", soln
