import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes=["SportsCpx","Siwaka","Ph.1A","Ph.1B","Phase2","STC","J1","Phase3","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()


#confirm nodes
#Add Edges and their weights
G.add_edge("SportsCpx","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("STC","Phase2",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Mada","ParkingLot",weight="700")
#position the nodes to resemble Nairobis map
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
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

#Add edge and node properties
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color='#c3b3ff', node_size=450)
nx.draw_networkx_edges(G, node_pos,width=1,edge_color='#000000')

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
