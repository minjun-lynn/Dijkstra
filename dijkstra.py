import copy

def find_min(X, Y):
    Z = copy.deepcopy(X)
    # print(X)
    for i in range(len(X)):
        if Y[i] == True:
            Z[i] = float("inf")
    x = min(Z)
    minindex = X.index(x)
    # print(X,Z)
    return minindex


#convert to a list of list of list,
#make the loop of numNodes to create outNode as [[],[],...]
#then loop through arcs to add value into outNode
def convert_arcList(arcList, numNodes):
    outNode = []
    outNode_cost = []

    for i in range(numNodes):
        outnode = []
        outnode_cost = []
        for k in range(len(arcList)):
            if arcList[k][0] == i:
                outnode.append(arcList[k][1])
                outnode_cost.append(arcList[k][2])
        outNode.append(outnode)
        outNode_cost.append(outnode_cost)
    # print(outNode)
    # print(outNode_cost)
    return outNode, outNode_cost

# def convert_arcList(arcList, numNodes):
#     outnode = []
#
#     for i in range(numNodes):
#         outnode.append([])
#
#     for k in range(len(arcList)):
#         index = arcList[k][0]
#         outnode[index] = [arcList[k][1],arcList[k][2]]
#
#     print(outnode)
#     return outnode

def dijkstra( numNodes, arcList, startNode ):
    """Dijkstra Algorithm
    Input:
    - numNodes: integer specifying the number of nodes.
      We'll assume that the nodes are labeled 0 ... numNodes - 1.
    - arcList: defines the arcs in the graph as a list of lists.
      arcList = [ [ fromNode1, toNode1, arcCost1], [ fromNode2, toNode2, arcCost2], ... ]
    - startNode = node ( in 0 to numNodes - 1 ) from where we want to find the shortest paths
    Output:
    - distances: List of length numNodes specifying the shortest path distance to each node (you can use float("inf") to represent infinity)
    - predecessors: List of length numNodes containing the predecessor on the shortest path for each node. ( you can use e.g. -1 to represent no predecessor)
    """

    # TO DO
    s = startNode
    distances = []
    predecessors = []
    cost = float("inf")
    numArc = len(arcList)
    permanent = []
    outNode, outNode_cost = convert_arcList(arcList, numNodes)


    for a in range(numNodes):
        distances.append(cost)
        permanent.append(False)
        predecessors.append(-1)

    distances[s] = 0


    #change correpond to convert_arcList
    for a in range(numNodes):
        minindex = find_min(distances, permanent)
        permanent[minindex] = True
        # print("Make node " + str(minindex) + " permanent")
        for i in outNode[minindex]:
            i_index = outNode[minindex].index(i)
            updatedistance = outNode_cost[minindex][i_index] + distances[minindex]
            if distances[i] > updatedistance:
                distances[i] = updatedistance
                predecessors[i] = minindex


    return distances, predecessors


## seven nodes, twelve arcs
if __name__ ==  "__main__":
    arcset = [[0,1,7], [0,2,2], [2,1,4], [1,3,2], [2,3,1], [1,4,2], [4,1,1], [2,5,5], [3,5,3], [3,4,1], [4,6,6], [5,6,2]]
    dis, prev = dijkstra(7,arcset,0)
    print(dis)
    print(prev)
