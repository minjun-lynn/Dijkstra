import unittest
import sys, os
# add source directory to path
# sys.path.append( os.path.abspath( '..' ))
import dijkstra

class TestDijkstra( unittest.TestCase ):

    def test_find_min( self ):
        distances = [1, 2, 3]
        permanent = [True, False, False]
        self.assertEqual( dijkstra.find_min(distances,permanent), 1)

    def test_convert_arcList( self ):
        arcList = [[0, 1, 1], [0, 3, 3], [1, 2, 2], [1, 3, 7], [2, 1, 4], [2, 3, 2]]
        numNodes = 4
        outNode = [[1, 3], [2, 3], [1, 3], []]
        outNode_cost = [[1, 3], [2, 7], [4, 2], []]
        self.assertEqual( dijkstra.convert_arcList(arcList, numNodes), (outNode, outNode_cost))

    def test_dijkstra( self ):
        numNodes = 4
        arcList = [[0, 1, 1], [0, 3, 3], [1, 2, 2], [1, 3, 7], [2, 1, 4], [2, 3, 2]]
        startNode = 0
        distances = [0, 1, 3, 3]
        predecessors = [-1, 0, 1, 0]
        self.assertEqual( dijkstra.dijkstra(numNodes, arcList, startNode), (distances, predecessors))


    # def test_approx_pca_init( self ):
    #     self.assertEqual( self.ap.dimLow, 3 )
    #     self.assertEqual( self.ap.percRow, 0.01 )
    #     self.assertEqual( self.ap.percCol, 1 )
    #     self.assertEqual( self.ap.minRow, 100 )
    #     self.assertEqual( self.ap.minCol, 150 )
