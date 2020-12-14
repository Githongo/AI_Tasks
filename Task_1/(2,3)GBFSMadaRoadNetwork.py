#import the necessary libraries
import os
import networkx as nx
import matplotlib.pyplot as plt
from classes.greedybfs import GBfsTraverser

G = nx.Graph()
nodes=["SportsCpx","Siwaka","Ph.1A","Ph.1B","Phase2","STC","Phase3","J1","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsCpx","Siwaka" ,distance=450)
G.add_edge("Siwaka","Ph.1A",distance=10)
G.add_edge("Siwaka","Ph.1B",distance=230)
G.add_edge("Ph.1A","Ph.1B",distance=100)
G.add_edge("Ph.1A","Mada",distance=850)
G.add_edge("Ph.1B","Phase2",distance=112)
G.add_edge("Ph.1B","STC",distance=50)
G.add_edge("STC","Phase2", distance=50)
G.add_edge("STC","ParkingLot",distance=250)
G.add_edge("Phase2","Phase3",distance=500)
G.add_edge("Phase3","ParkingLot", distance=350)
G.add_edge("Phase2","J1", distance=600)
G.add_edge("J1","Mada",distance=200)
G.add_edge("Mada","ParkingLot", distance=10)
#position the nodes to Madaraka Estate Network
G.nodes["SportsCpx"]['pos']=(-30,9)
G.nodes["Siwaka"]['pos']=(10,9)
G.nodes["Ph.1A"]['pos']=(35,9)
G.nodes["Ph.1B"]['pos']=(35,-10)
G.nodes["Phase2"]['pos']=(80,-10)
G.nodes["J1"]['pos']=(105,-10)
G.nodes["Mada"]['pos']=(135,-10)
G.nodes["STC"]['pos']=(35,-30)
G.nodes["Phase3"]['pos']=(105,-30)
G.nodes["ParkingLot"]['pos']=(105,-52)

#getting heuristics from txt file
def getHeuristics(G):
    heuristics = {}
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, 'heuristics.txt'))
    for i in G.nodes():
        node_heuristic_val = f.readline().split()
        heuristics[node_heuristic_val[0]] = node_heuristic_val[1]
    return heuristics

heuristics = getHeuristics(G)
node_pos = nx.get_node_attributes(G,'pos')

#call BFS
route_bfs = GBfsTraverser()
routes = route_bfs.GBFS(G,heuristics,"SportsCpx","ParkingLot")


route_list = route_bfs.path
#color the nodes and edges in the route_bfs
node_col = ['#c3b3ff' if not node in route_list else '#69f591' for node in G.nodes()]
green_colored_edges = list(zip(route_list,route_list[1:]))
edge_col = ['#000000' if not edge in green_colored_edges else '#2dc458' for edge in G.edges()]
arc_label=nx.get_edge_attributes(G,'label')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_label)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels={('SportsCpx','Siwaka'):'UnkRoad(450m)',
   ('Siwaka','Ph.1A'):'SangaleRd(10m)',('Siwaka','Ph.1B'):'SangaleLink(230m)',('Ph.1A','Ph.1B'):'ParkingWalkWay(100m)',('Ph.1B','Phase2'):'KeriRd(112m)',
   ('Phase2','J1'):'KeriRd(600m)',('J1','Mada'):'SangaleRd(200m)',('Ph.1A','Mada'):'SangaleRoad(850m)',('Ph.1B','STC'):'KeriRd(50m)',
   ('STC','Phase2'):'STCwalkway(50m)',('Phase2','Phase3'):'KeriRd(500m)',('Phase3','ParkingLot'):'HimaGRd(350m)',('STC','ParkingLot'):'LibraryWalkWay(250m)',
   ('ParkingLot','Mada'):'LangataRd(700m)'},font_color='#000000',font_size='x-small')
plt.axis('off')
plt.show()