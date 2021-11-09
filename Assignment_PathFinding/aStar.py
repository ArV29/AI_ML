pathsAndCosts = {'A' : {'B' : 2, 'E' : 3,},
         'B' : {'A' : 2, 'C' : 1, 'G':9},
         'C' : {'B' : 1},
         'D' : {'E' : 6, 'G' : 1},
         'E' : {'A' : 3, 'D' : 6},
         'G' : {'B' : 9, 'D' : 1}}

positions = { 'A' : (1, 0), 
              'B' : (0, 1),
              'C' : (0, 2),
              'D' : (2, 2),
              'E' : (2, 1),
              'G' : (1, 3)}


def findH(nodeA, nodeB):
  h = ((positions[nodeA][0] - positions[nodeB][0])**2 + (positions[nodeA][1] - positions[nodeB][1])**2)**0.5
  return h

def findNewNodes(currentNode, currentCost, priorityQueue, visited, endNode):
  for node in pathsAndCosts[currentNode]:
    if not node in visited:
      g = currentCost+pathsAndCosts[currentNode][node]
      h = findH(node, endNode)
      if node in priorityQueue:
        if priorityQueue[node][0] > g+h:
          priorityQueue[node] = (g, h, currentNode)
      else:
        priorityQueue[node] = (g, h, currentNode)
  
def findNextNode(priorityQueue):
  minCost = 1000000000
  selectedNode = None
  for node in priorityQueue:
    cost = priorityQueue[node][0] + priorityQueue[node][1]
    if cost< minCost:
      minCost = cost
      selectedNode = node
  return selectedNode

def run(startNode, endNode):
  priorityQueue = {startNode : [0, 0, 0]}
  selectedNode = startNode
  visited = {startNode:0}
  cost = 0
  while selectedNode != endNode:
    findNewNodes(selectedNode, cost, priorityQueue, visited, endNode)
    priorityQueue.pop(selectedNode)
    nextNode = findNextNode(priorityQueue)
    cost = priorityQueue[nextNode][0]
    visited[nextNode] = priorityQueue[nextNode][2]
    selectedNode = nextNode
  path = []
  prevNode = endNode
  while prevNode != 0:
    path.append(prevNode)
    prevNode = visited[prevNode]
  return cost, path

def main():
  start = input('Enter Start Point: ')
  end =  input('Enter End Point: ')
  cost, path = run(start, end)
  print('Route Cost:', cost)
  print('Best Path:', *reversed(path))

def result():
  print('Automatic cost calculation for each node against every other node!')
  print('\n\n\n')
  nodes = {"A": 1, "B":2, "C":3, "D":4, "E":5, "G":6}
  result = [[' ', 'A', 'B', 'C', 'D', 'E', 'G'],
            ['A', -1, -1, -1, -1 ,-1 ,-1],
            ['B', -1, -1, -1, -1 ,-1 ,-1],
            ['C', -1, -1, -1, -1 ,-1 ,-1],
            ['D', -1, -1, -1, -1 ,-1 ,-1],
            ['E', -1, -1, -1, -1 ,-1 ,-1],
            ['G', -1, -1, -1, -1 ,-1 ,-1]]
  for i in nodes:
    for j in nodes:
      if i == j:
        continue
      result[nodes[i]][nodes[j]] = run(i, j)[0]
  for i in result:
    print(*i)
  print('\n\n\n')


if __name__ == "__main__":
  result()
  main()
