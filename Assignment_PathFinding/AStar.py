grid = [[0, 'B', 'C', 0],
        ['A', 0, 0, 'G'],
        [0, 'E', 'D', 0]]

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

heuristics = {'A' : {'A' : 0,
                     'B' : 2, 
                     'C' : 3,
                     'D' : 9,
                     'E' : 3,
                     'G' : 10},
              'B' : {'A' : 2,
                     'B' : 0, 
                     'C' : 1,
                     'D' : 10,
                     'E' : 5,
                     'G' : 9},
              'C' : {'A' : 3,
                     'B' : 1, 
                     'C' : 0,
                     'D' : 11,
                     'E' : 6,
                     'G' : 10},
              'D' : {'A' : 9,
                     'B' : 10, 
                     'C' : 11,
                     'D' : 0,
                     'E' : 6,
                     'G' : 1},
              'E' : {'A' : 3,
                     'B' : 5, 
                     'C' : 6,
                     'D' : 6,
                     'E' : 0,
                     'G' : 7},
              'G' : {'A' : 10,
                     'B' : 9, 
                     'C' : 10,
                     'D' :1,
                     'E' : 7,
                     'G' : 0}}



def findNextNode(currentNode, visited, blackList,  endNode, currentCost):
  nextNode = None
  for i in pathsAndCosts[currentNode]:
    if i in visited or i in blackList:
      continue
    gI = currentCost + pathsAndCosts[currentNode][i]
    hI = heuristics[endNode][i]
    bestF= gI+ hI
    nextNode = i
    break
  
  for i in pathsAndCosts[currentNode]:
    if i in visited or i==nextNode or i in blackList:
      continue
    gI = currentCost + pathsAndCosts[currentNode][i]
    hI = heuristics[endNode][i]
    fI = gI + hI
    if fI< bestF:
      bestF= gI+ hI
      nextNode = i
  
  return nextNode
  

    

def findRoute(start, end):
  currentNode = start
  visited = {start}
  blackList = set()
  cost = 0
  nextNode = findNextNode(currentNode, visited, blackList, end, 0)
  cost += pathsAndCosts[currentNode][nextNode]
  prevNode = currentNode
  while nextNode != end:
    prevNode = currentNode
    currentNode = nextNode
    nextNode = findNextNode(currentNode, visited, blackList, end, cost)
    if nextNode == None:
      blackList.add(currentNode)
      nextNode = prevNode
      continue
    visited.add(nextNode)
    cost += pathsAndCosts[currentNode][nextNode]
  
  return (cost)


def main():
  start = input("Starting Node: ")
  end = input("Destination Node: ")


def result():
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
      result[nodes[i]][nodes[j]] = findRoute(i, j)
    
  for i in result:
    print(*i)

if __name__ == "__main__":
  result()
