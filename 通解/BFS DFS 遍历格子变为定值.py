DFS:
  def dfs(x,y):
    grid[x][y]='a'
    for i,j in [(),()...]:
      if 0<i+x<=len(grid) and 0<j+y<=len(grid[0]) and grid[][]=='0':
        dfs(i+x,j+y)
        
 BFS:####注意需要visited记录已经遍历过的格子
  def bfs(x,y):
    queue=deque([x,y])
    visited={(x,y)}
    while queue:
      x,y=queue.popleft()
      gird[x][y]='a'
      for i,j in [().()...]:
        if 0<x+i<=len(grid) and  0<j+y<=len(grid[0]) and grid[][]=='0'and () not in visited:
          queue.append((x+i,j+y))
          visited.add(())
      
      
      
      
