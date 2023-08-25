#Connor Marks 

import csv

#reads entries from csv file, this comes from kruskal's implementation on the assignment sheet
with open('input.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  line = next(csv_reader)


number_of_vertices = int(line[0])

#loop through the values found in the csv files
graph = [[0 for i in range(number_of_vertices)]
         for j in range(number_of_vertices)]
edges = []
vertices = []
k = 0

#creates the adjacency matrix
count = 0
for i in range(0, number_of_vertices):
  for j in range(0, number_of_vertices):
    k = k + 1
    graph[i][j] = int(line[k])
    count += 1

    # append nonzero edges to the matrix
    if (int(line[k]) != 0):
      edges.append((int(line[k]), i, j))


selected_vertices = []
selected_edges = []
selected_vertices.append(0)  # start with arbitrary vertex 0, append it to the selected_vertices

#STEPS 
# 1) Start with an arbitrary vertex (in this case it is 0), then append it to the selected_vertices
# 2) All subgraphs are connected, so I search for all vertices that are adjacent to the selected one in the adjacency matrix and append the adjacent vertex with the cheapest edge to selected_edges
# 3) Since the adjacent vertex was not used yet, append edges[2] (the second vertex) to selected_vertices.
# 4) The minimum-weighted spanning tree must use all vertices, so a while loop can be used to continue iterating until the number of elements in selected_vertices is equal to the number of vertices in the original graph 

#edges[0][0] contains information about (weight of edge,vertex,vertex2)

#pick all of the cheapest edges to append to the set 

#cycle detection is factored in automatically

#condition for spanning tree: use every vertex, no cycles.
#While I haven't used every vertex, find the minimum cost edge connecting unused vertices
while len(selected_vertices) != number_of_vertices:
  min_edge = None
  #edges[row][0] = weight of edge, edges[row][1] = vertex1, edges[row][2] = vertex2
  for edge in edges:
    #this logic checks if the two vertices are adjacent, if not, run the nested if statement. This also automatically ensures no cycles can be produced since only vertices that were not previously in the subgraph can be appended. 
    if edge[1] in selected_vertices and edge[2] not in selected_vertices:
      
      #check that if the edge weight is less than the min_edge weight at that index,assign the minimum edge to be that edge 
      
      if min_edge == None or edge[0] < min_edge[0]:
        min_edge = edge
  #append the minimum edge to selected edges 
  selected_edges.append(min_edge)
  #append vertex 2 to the selected vertices 
  selected_vertices.append(min_edge[2])

#print statement
weight = 0
print(f"{number_of_vertices} vertices found")
for edge in selected_edges:
  print(f"Adding edge ({edge[1]}, {edge[2]}) with weight {edge[0]}")
  weight += edge[0]
print(f"Total weight of spanning tree: {weight}")

# graph[0][0] -> represents [7,0,2]
# graph[0][1]-> represents [8,0,3]
# graph[0][2] -> represents [6,0,4]

# graph[1][0] -> represents [7,0,5]
# graph[1][1] -> represents [14,0,6]
# graph[1][2] -> represents [13,0,7]

# length of the rows are always 3 
# graph[i][j] -> represents [edge weight, vertex1, vertex 2]


#outer loop is the number of rows

