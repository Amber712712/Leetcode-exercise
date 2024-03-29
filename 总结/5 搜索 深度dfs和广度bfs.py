BFS 使用Queue
模板：二叉树的层级模式(step, 层级分别是哪些，层级最大)
step=0
visited=set()
while queue:
      for i in range(len(queue)):
          x=queue.pop(0)/popleft()
          
三要素：QUEUE pop 以及visited
##注意最小距离和最大距离（最小距离）所使用的step是不一样的 
最小距离：需要和i,j,s一起入queue    最大距离（最小距离）：直接用step计数


1 对于最小路径问题，求最短路径不管是图，还是其他step
bfs适应性很强 : 使用queue while queue 作为标志
def func(grid):
    if grid[0][0]==1 or grid[-1][-1]==1:
       return -1
    if len(grid)<=2:
       return len(grid)
    queue=[(0,0,1)]
    grid[0][0]=1
    while queue:
       i,j,s=queue.pop(0)
       for i1,j1 in [(),(),...]:
           if i+i1==len(grid)-1 and j+j1==len(grid)-1:
              return step+1
           if 0<=i+i1<len(grid) and 0<=j+j1<len(grid) and grid[i+i1][j+j1]==0:
              grid[i+i1][j+j1]=1
              queue.append((i+i1,j+j1,s+1))
    return -1
            
    

2 整数最少分成的平方数     二叉树层级遍历  
def func(nums):
    Q=collections.deque()
    visited=set()
    step=1
    Q.append(nums)
    while Q:
         n=len(Q)
         for i in range(n):
             x=Q.popleft()
             for y in range(1,int(sqrt(nums)+1)):
                 t=x-y**2
                 if t==0:
                    return step
                 elif t not in visited:
                    visited.add(t)
                    Q.append(t)   #####注意需要添加新的queue值
         step+=1
          return step
          
 3 层级遍历二叉树 
 def func(root):
 queue=collections.deque()
 queue.append(root)
 res=[]
 if not root:
    return []
 while queue:
       level=[]
       for i in range(len(queue)):
           r=queue.popleft()
           level.append(r.val)
           if not r.left:
              queue.append(r.left)
           if not r.left:
              queue.append(r.right)
        
        res.append(level)
 4 求二叉树层级最大值
 def func(root):
     queue=collections.deque()
     queue.append(root)
     res=[]
     while queue:
           max1=float('-inf')
           for i in range(len(queue)):
               r=queue.popleft()
               
               max1=max(max1,r.val)
               if not r.left:
              queue.append(r.left)
               if not r.left:
              queue.append(r.right)
           res.append(max1)
     return res
     
5 岛屿与陆地最大的距离（指最小的距离）
def func(grid):
    n=len(grid)
    step=0
    queue=[[i,j] for i in range(n) for j in range(j) if grid[i][j]==1]
    if len(queue)==0 or len(queue)==n**2:
       return -1
    while queue:
          for i in range(len(queue)):
              x,y=queue.popeleft()
              for x1,y1 in [()....]:
                  if 0<x+x1<n and 0<y+y1<n and grid[x+x1][y+y1]==0:
                     
                     grid[x+x1][y+y1]==-1
                     queue.append([x+x1,y+y1])  
              step+=1
          return step-1 #######注意这里曾多加了一个
          
    
     


深度搜索 dfs (递归)
dfs:
树的最大高度
dfs:
def func(root):
      if not root:
            return 0
      return max(func(root.left),func(root.right))+1
Bfs:
def func(root):
      if not root:
            return 0
      queue=[root]
      step=0
      while queue:
            for i in range(len(queue)):
                  r=queue.pop(0)
                  if r.left:
                        queue.append(r.left)
                  if r.right:
                        queue.append(r.right)
             step+=1
      return step
                  

树的最小高度



注意递归的结束条件  不符合条件时return 0

1 最大海岛面积
def func(grid):
r=len(grid) 
c=len(grid[0])
res=0
def dfs(i,j):
    if i<0 or i==r or j<0 or j==c or grid[i][j]!=1:
       return 0
    grid[i][j]=0
    return 1+dfs(i+1,j)+dfs(i-1,j)+...
   
for i in range(r):
    for j in range(c):
        res=max(res,dfs(r,c))
return res

也可用bfs做： 
def func(grid):
    def bfs(i,j):
        grid[i][j]=0
        queue=[(i,j)]
        area=1
        while queue:
              for x,y in [(),()...]:
                  if 0<=i+x<len(gird) and 0<=j+y<len(gird[0]) and grid[i+x][j+y]==1:
                     grid[][]=0
                     area+=1
                     queue.append((i+x,y+j))
        return area
     res=0
     for i in range():
         for j in range():
             if grid[i][j]==1:
                res=max(res,bfs(i,j))

2 海岛数量
def func(grid):
    r=len(grid) 
    c=len(grid[0])
    def dfs(i,j):
        if i<0 or i==r or j<0 or j==c or grid[i][j]!=1:
           return 0
        grid[i][j]=0
        dfs(i+1,j)
        dfs(i-1,j)
        ...
        
     count=0
     for i in range(r):
         for j in range(c):
             if grid[i][j]=="1":
                dfs(i,j)
                count+=1
     return count
     
     
     
3 连通的海岛数量
目的是创造visited, 并不断更新visited

def func(grid):
    visited=set()
    count=0
    
    def dfs(i):
        for j in range(len(grid)):
            if grid[i][j]==1 and j not in visited:
               visited.add(j)
               dfs(j)
               
    for i in range(len(grid)):
        if i not in visited:
           dfs(i)
           count+=1
return count

4 除了边界上的0，其他被包围的0要变为x
利用dfs来将符合条件的格子标志

x x x x   
x 0 0 x
x x x x
x 0 x x

def func(grid):
    if not grid:
       return []
    def dfs(i,j):
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j]!="0":
           return []
        grid[i][j]="A"
        dfs(i+1,j)
        dfs(i-1,j)
        ...
  ##method 2
    def dfs(i,j):
            grid[][]=='1' ####需要在这里转换格子
            for x,y in [(),()...]:
                  if 0<i+x<=len(grid) and 0<j+y<=len(grid[0]) and grid[][]=="0":
                        
                        dfs(i+x,j+y)
                        
        
        for i in range(len(grid)):
            dfs(i,0)
            dfs(i,len(grid[0]))
        for j in range(len(grid[0]):
            dfs(0,i)
            dfs(len(grid),i)
            
        for i in range():
            for j in range():
                if grid[i,j]="A":
                   grid[i,j]="0"
                elif grid[i,j]="0":
                     grid[i,j]="X"
                     
    
    
5 太平洋大西洋交汇处
def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pacific=[[0]*n for i in range(m)]
        atlantic=[[0]*n for i in range(m)]
        dis=[[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(m):
            pacific[i][0]=1
        for i in range(n):
            pacific[0][i]=1
        for i in range(m):
            atlantic[i][n-1]=1
        for i in range(n):
            atlantic[m-1][i]=1
        def dfs1(r,c):
            for i in dis:
                x=r+i[0]
                y=c+i[1]
                if 0<=x<=m-1 and 0<=y<=n-1 and heights[x][y]>=heights[r][c] and pacific[x][y]==0:
                    pacific[x][y]=1
                    dfs1(x,y)
        def dfs2(r,c):
            for i in dis:
                x=r+i[0]
                y=c+i[1]
                if 0<=x<=m-1 and 0<=y<=n-1 and heights[x][y]>=heights[r][c] and atlantic[x][y]==0:
                    atlantic[x][y]=1
                    dfs2(x,y)
        for i in range(m):
            dfs1(i,0)
        for i in range(n):
            dfs1(0,i)
        for i in range(m):
            dfs2(i,n-1)
        for i in range(n):
            dfs2(m-1,i)
        ans=[]
        for i in range(m):
            for j in range(n):
                if pacific[i][j]==1 and atlantic[i][j]==1:
                    ans.append([i,j])
        return ans
