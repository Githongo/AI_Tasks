from queue import PriorityQueue
import queue as Q
import networkx as nx


class Ucs:
    def __init__(self):
        self.visited = []
        self.end_search = False

    def get_cost(self, graph, from_node, to_node):
        cost = nx.get_edge_attributes(graph, 'weight')
        return int(cost[(from_node, to_node)])

    def ucs(self, graph, start_node, goal_node):
        visited = set()
        queue = Q.PriorityQueue()
        queue.put((0, start_node))

        while queue and not self.end_search:
            cost, node = queue.get()
            if node not in self.visited:
                self.visited.append(node)

                if node == goal_node:
                    print("We have reached ", node, " the final destination")
                    self.end_search = True
                    break
                for i in list(graph[node]):
                    if i not in self.visited:
                        print('start')
                        print(i)
                        print('end')
                        total_cost = cost + self.get_cost(graph, node, i)
                        queue.put((total_cost, i))
            else:
                print(node)
        print("Final path: ", self.visited)
