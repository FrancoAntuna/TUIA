# Podemos también graficar los grafos. Vamos a usar la función plot_graph que definimo aquí debajo
import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G):
    """
    funcion auxiliar para imprimir los grafos con los que trabajemos
    El peso de las aristas, si los hay, debe estar en el atributo 'weight'
    """

    try:
      pos = nx.planar_layout(G)
    except:
      pos = nx.spring_layout(G, seed=0, pos=pos, iterations=it)

    nx.draw_networkx_nodes(G,pos, node_color='lightblue', node_size=100)
    edge_labels=dict([((u,v,),d.get('weight', ''))
            for u,v,d in G.edges(data=True)])
    nx.draw_networkx_labels(G,pos, font_size=8,font_family='sans-serif')
    nx.draw_networkx_edges(G,pos, width=0.4, )
    plt.axis('off')
    #nx.draw_networkx_labels(self.G,pos, font_size=20,font_family='sans-serif')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels, verticalalignment="top", horizontalalignment="right")
    nx.draw(G,pos, edge_cmap=plt.cm.Reds)

    plt.show()

#Podemos crear un grafo
G1 = nx.Graph ()

#Podemos agregar nodos de a uno, por ejemplo
G1.add_node (1)

#o de a varios a la vez
G1.add_nodes_from ([2 , 3])

#Podemos agregar aristas de a una, utilizando dos sintaxis distintas
G1.add_edge (1 , 2)
# o bien
e = (2 , 3)
G1.add_edge (*e)

#vamos viendo el grafo
plot_graph(G1)

#o de a varias a la vez
G1.add_edges_from ([(3 , 4) , (5 , 6)])
plot_graph(G1)

#Podemos ver cuantos nodos y cuantas aristas tiene nuestro grafo utilizando los métodos asociados
G1.number_of_nodes () # 6
G1.number_of_edges () # 4

#También podemos obtener la lista completa de nodos y de aristas que contiene un grafo:
list(G1.nodes) # [1, 2, 3, 4, 5, 6]
list(G1.edges) # [(1, 2), (2, 3), (3, 4), (5, 6)]

dict(G1.degree) # {1: 1, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1}

#Del mismo modo que agregamos nodos y aristas, podemos removerlos, utilizando las funciones apropiadas
G1.remove_node(2)
plot_graph(G1)

G1.remove_nodes_from ([3,4])
plot_graph(G1)

G1.remove_edge(5, 6)
plot_graph(G1)

#Si queremos que nuestros grafos tengan peso en las aristas, utilizamos el parámetro especial weight al momento de agregarla
G1.add_edge (1 , 2 , weight =4.7 )

plot_graph(G1)

G2 = nx . Graph ()
G2.add_nodes_from ([1 , 2 , 3])
G2.add_edges_from ([(1 , 2) , (1 , 3)])
G2.add_node ("spam") # adds node " spam "

plot_graph(G2)


#Podemos encontrar la longitud del camino mas corto entre dos vértices utilizando el m ́etodo shortest path length y un camino de esa longitud
#(expresado como una secuencia de vértices) con el método shortest path.

#Nota: Si en los métodos omitimos el parámetro weight, interpretará que todos los pesos son iguales a 1. Para que tome los pesos que asignamos a las aristas,
#debemos pasar explícitamente weight="weight"
import math

G3 = nx.Graph ()
G3.add_nodes_from ( "abcdefghijz" )
G3.add_edge ( "a" , "b" , weight =4)
G3.add_edge ( "b" , "c" , weight =1)
G3.add_edge ( "c" , "d" , weight =6)
G3.add_edge ( "b" , "e" , weight =6)
G3.add_edge ( "b" , "f" , weight =4)
G3.add_edge ( "c" , "f" , weight =3)
G3.add_edge ( "d" , "z" , weight =1)
G3.add_edge ( "a" , "e" , weight =1)
G3.add_edge ( "f" , "e" , weight =6)
G3.add_edge ( "f" , "g" , weight =5)
G3.add_edge ( "g" , "h" , weight =1)
G3.add_edge ( "a" , "i" , weight =6)
G3.add_edge ( "e" , "j" , weight =8)
print( nx.shortest_path_length (G3 , source = "a" , target = "z" , weight = "weight "))
print( nx.shortest_path (G3 , source = "a" , target = "z" , weight = "weight "))

plot_graph(G3)


#Podemos encontrar un  árbol de expansión utilizando el algoritmo DFS mediante el método dfs tree.
G4 = nx . Graph ()
G4.add_nodes_from ("abcdef")
G4.add_edge ( "a" , "b" , weight =4)
G4.add_edge ( "b" , "c" , weight =1)
G4.add_edge ( "c" , "d" , weight =6)
G4.add_edge ( "b" , "e" , weight =6)
G4.add_edge ( "b" , "f" , weight =4)
G4.add_edge ( "c" , "f" , weight =3)
G4.add_edge ( "d" , "a" , weight =1)
G4.add_edge ( "a" , "e" , weight =1)
G4.add_edge ( "f" , "e" , weight =6)
G4.add_edge ( "f" , "b" , weight =5)
G4.add_edge ( "c" , "d" , weight =1)
G4.add_edge ( "a" , "e" , weight =6)
G4.add_edge ( "e" , "f" , weight =8)
plot_graph(G4)

T = nx . dfs_tree (G4 , source = 'a')
plot_graph( T )

