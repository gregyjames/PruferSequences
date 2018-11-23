import graphClass
import networkx as nx
import matplotlib.pyplot as plt
import warnings

#Filter all matplotlib warnings
warnings.filterwarnings("ignore")

#Find the leaf with the lowest label
def findLowestLeaf(G):
    #Empty array of vertexes
    vertexes = []
    #Look through every vertex of the graph
    for x in G.vertList:
        #Return the lowest number vertex with the 1 adjacent vertex (leaf)
        if len(G.getVertex(x).getAdj()) == 1:
            vertexes.append(x);
    #Return the first element of the list, thus the lowest leaf
    return sorted(vertexes)[0]

#Convert a graph to a prufer sequence
def graphToPrufer(G):
    #Empty array to hold the sequence
    sequence = []
    graph = G

    while len(graph.getVertices()) > 2:
        lowest = findLowestLeaf(graph)
        sequence.append(graph.getVertex(lowest).getAdj()[0].id)
        graph.delVertex(lowest)
    return sequence

#Find the lowest index in a dictionary
def findLowest(table, list_size):
    index = 0;

    for i in range(1, list_size + 1):
        if(table[i] == 1):
            index = i;
            break;

    table[index] = table[index] - 1;

    return index;

def checkForOnes(table):
    return 1 in table.values();

#Convert a Prufer sequence to a Graph
def PruferToGraph(list):
    list_size = len(list) + 2
    table = {}
    #Create Empty Graph object
    G = nx.Graph()

    #Fill the empty table with values from 1..n+2 with one
    for x in range(1,list_size + 1):
        table[x] = 1
        G.add_node(x)

    #Fill the table with the counts from the list + 1
    for x in list:
        count = 0;
        for y in list:
            if x == y:
                count = count + 1
        table[x] = count + 1

    while len(list) > 0:
        #for every element in the sequence
        for x in range(1, len(list) + 1):
            #Find and remove the lowest number from the tree
            low = findLowest(table, list_size);
            G.add_edge(low, list[0])
            #Minus one count from the corresponding list element on the table
            table[list[0]] = table[list[0]] - 1;
            #Delete the item from the list
            del list[0]
            break;

    #The loop above leaves two vertexs remaining in the dictionary
    #This uses them to make the last edge of the graph
    last_edge_v1 = findLowest(table, list_size)
    last_edge_v2 = findLowest(table, list_size)
    G.add_edge(last_edge_v1, last_edge_v2)

    #Draw the graph
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    return table

#Build the graph from the counting trees ws
P = graphClass.Graph()
for i in range(1,15):
    P.addVertex(i)
p = P.vertList[1]
P.addEdge(9,1)
P.addEdge(9,2)
P.addEdge(10,3)
P.addEdge(10,4)
P.addEdge(11,5)
P.addEdge(11,6)
P.addEdge(12,7)
P.addEdge(12,8)
P.addEdge(13,9)
P.addEdge(13,10)
P.addEdge(14,11)
P.addEdge(14,12)
P.addEdge(15,13)
P.addEdge(15,14)

#Convert the graph into a sequence
prufer = graphToPrufer(P)

#Convert a sequence to a graph
PruferToGraph(prufer)
