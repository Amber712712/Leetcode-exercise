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
        
 2 
261 树是否有环 利用dfs+visited 从0到n-1
如果边数>顶点数-1，肯定有环，如果小于，肯定有不连通

s="(A,B)(B,C)(C,D)"
def func(s):
  if s[0] or s[-1]==" ":
    return E1
  
def func(n,lists):
  if len(lists)!=n-1:
    return False
  dic=defaultdict(list)
  for x,y in lists:
    dic[x].append(y)
    dic[y].append(x)

  visited=[False for _ in range(n)]
  BFS：
  Q=collections.deque()
  Q.append(0)
  while Q:
    x=Q.popleft()
    visited[x]=True
    for y in dic[x]:
      if visited[y]==False
      Q.append(y)
      
  
  #DFS：
  def dfs(x):
    visited[x]=True
    for i in dic[x]:
      if visited[i]=False:
        dfs(i)
      
  for n in range(n):
    if visited[n]==False:
      return False
  return True

        
      


      

  
  



        

  
  
