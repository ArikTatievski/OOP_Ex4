from unittest import TestCase
from GraphAlgo import *
from DiGraph import *
from Node import *
from Edge import *


class TestGraphAlgo(TestCase):

    def test_shortest_path(self):
        g = DiGraph()
        g.add_node(0, (1, 1))
        g.add_node(1, (1, 1))
        g.add_node(2, (1, 1))
        g.add_node(3, (1, 1))
        g.add_node(4, (1, 1))
        g.add_node(5, (1, 1))
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 4, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(4, 0, 3)
        g.add_edge(4, 3, 6)
        g.add_edge(2, 1, 5)
        g.add_edge(3, 5, 1)
        g.add_edge(5, 4, 8)
        g.add_edge(5, 2, 10)
        gh = GraphAlgo(g)
        shortestPath = gh.shortest_path(0,2)
        self.assertEqual(shortestPath[0],2)
        self.assertEqual(shortestPath[1],[0,1,2])

    def test_tsp(self):
        g = DiGraph()
        g.add_node(0, (1, 1))
        g.add_node(1, (1, 1))
        g.add_node(2, (1, 1))
        g.add_node(3, (1, 1))
        g.add_node(4, (1, 1))
        g.add_node(5, (1, 1))
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 4, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(4, 0, 3)
        g.add_edge(4, 3, 6)
        g.add_edge(2, 1, 5)
        g.add_edge(3, 5, 1)
        g.add_edge(5, 4, 8)
        g.add_edge(5, 2, 10)
        gh = GraphAlgo(g)
        tspAns = gh.TSP([0,1,2,4])
        self.assertEqual(tspAns[0],[0,1,2,1,4])
        self.assertEqual(tspAns[1], 8)

    def test_center_point(self):
        g = DiGraph()
        g.add_node(0, (1, 1))
        g.add_node(1, (1, 1))
        g.add_node(2, (1, 1))
        g.add_node(3, (1, 1))
        g.add_node(4, (1, 1))
        g.add_node(5, (1, 1))
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 4, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(4, 0, 3)
        g.add_edge(4, 3, 6)
        g.add_edge(2, 1, 5)
        g.add_edge(3, 5, 1)
        g.add_edge(5, 4, 8)
        g.add_edge(5, 2, 10)
        gh = GraphAlgo(g)
        self.assertEqual((0, 2), gh.centerPoint())