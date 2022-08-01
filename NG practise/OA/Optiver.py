1 Search a Word in a 2D Grid of  (BFS搜索)
def func(grid,target):
  if not grid:
    return 
  dic=[[0,1],[0,-1],[1,0],[-1,0]]
  def bfs(grid,row,col,t):
    unlocal dic
    flag=True
    if grid[row][col]!=t[0]:
      return False
    for x,y in dic:
      xi,yi=row+x,col+y
      for n in range(1,len(t)):
        if 0<=xi<len(grid) and 0<=yi<len(grid[0]) and grid[xi][yi]==t[n]:
          xi+=x
          yi+=y
        else:
          flag=False
          break
    return flag
      

    
  m=len(grid)
  n=len(grid[0])
  for i in range(m):
    for j in range(n):
      if bfs(grid,row,col,t):
        print("pattern found at " +str(row) + ', ' + str(col))
        

  
  
