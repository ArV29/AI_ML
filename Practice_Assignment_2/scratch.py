nodes = {0: [1, 2], 1: [2, 3], 2: [3], 3: [4], 4: [0, 1, 5], 5:[]}


def bfs(root):
  print('\n\nBFS route: ')
  visitedNodes = set()
  queue = [root]
  visitedNodes.add(root)
  result = ''
  while queue:
    s = queue.pop(0)
    result += (str(s)+' -> ')
    for i in nodes[s]:
      if not i in visitedNodes:
        queue.append(i)
        visitedNodes.add(i)
  result += 'END'
  print(result, '\n\n')
    


def dfs(root, visitedNodes, route):
  visitedNodes.add(root)
  route.append(root)
  for children in nodes[root]:
    if not children in visitedNodes:
      dfs(children, visitedNodes, route)

def startDfs(root):
  print('DFS route: ')
  visitedNodes = set()
  route = []
  dfs(root, visitedNodes, route)

  for i in route:
    print (i, '->', end = ' ')
  print('END\n\n')

bfs(0)
startDfs(4)
