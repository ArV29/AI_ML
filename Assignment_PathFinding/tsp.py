import random
costs = [[0, 7, 12, 10, 13],
        [7, 0, 14, 10, 12],
        [12, 14, 0, 14, 9],
        [10, 10, 14, 0, 7],
        [13, 12, 9, 7, 0]]

      
def randomRoute(start):
  cities = [0, 1, 2, 3, 4]
  cities.remove(start)
  randomSolution = [start]
  for i in range(len(cities)):
    next = cities[random.randrange(0, len(cities))]
    randomSolution.append(next)
    cities.remove(next)
  return randomSolution

def calculateRouteLength(route):
  length = 0
  for i in range(len(route)-1):
    length += costs[route[i]][route[i+1]]
  length += costs[route[-1]][0]
  return length

def generateNeighbors(route):
  neighbors = []
  for i in range(1, len(route)):
    for j in range(i+1, len(route)):
      neighbor = route.copy()
      neighbor[i] = route[j]
      neighbor[j] = route[i]
      neighbors.append(neighbor)
  return neighbors


def getBestNeighbor(neighbors):
  bestCost = calculateRouteLength(neighbors[0])
  bestNeighbor = neighbors[0]
  for i in range(1, len(neighbors)):
    cost = calculateRouteLength(neighbors[i])
    if cost<bestCost:
      bestNeighbor = neighbors[i]
      bestCost = cost
  return (bestNeighbor, bestCost)


def tSP(start):
  currentSol = randomRoute(start)
  currentCost = calculateRouteLength(currentSol)
  neighbors = generateNeighbors(currentSol)
  bestNeighbor, bestCost = getBestNeighbor(neighbors)
  visitedPaths = {list2String(currentSol)}
  while bestCost <= currentCost:
    visitedPaths.add(list2String(bestNeighbor))
    currentSol = bestNeighbor
    currentCost = bestCost
    neighbors = generateNeighbors(currentSol)
    bestNeighbor, bestCost = getBestNeighbor(neighbors)
    if list2String(bestNeighbor) in visitedPaths:
      break

  cities = ['A', 'B', 'C', 'D', 'E']
  for i in currentSol:
    print(cities[i], '->', end= '')
  print(cities[currentSol[0]])
  print("Cost: ", currentCost)


def main():
  start = (input("Enter Starting Location: "))
  nodes = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

  tSP(nodes[start])


def list2String(list):
  s =''
  for i in list:
    s+=str(i)
  return s
if __name__ == "__main__":
  main()
