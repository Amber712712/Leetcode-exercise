1 三角形 do they belong
def func(x1,y1,x2,y2,x3,y3,x,y):
  l1=sqrt((x1-x2)**2+(y1-y2)**2)
  l2=
  
  def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)
查看三角形面积之和是否一样

2 points里的每个整数必须+k或-k，并返回新的points里最大值和最小值之差的最小可能值
def func(points):
  points.sort()
  for i in range(len(points)):
    min1=points[0]+k
    max1=points[i]+k
    min2=points[i+1]-k
    max2=points[len(points)-1]-k
    
    
3 m次方相乘得到一个值，把每个s[i]的该值相加得到一个和，返回这个和是奇数还是偶数

4 group friend
def func(n,q,s1,s2):
  dic=defualtdict(list)
  for i in range(len(q)):
    if q[i]=='friend':
      dic[s1[i]]=s2[i]
      dic[s2[i]]=s1[i]
    else:
      f1=s1[i]
      f2=s2[i]
   
  visited=[False for i in range(n)]
  def circle(n):
    Q=collections.deque()
    Q.append(n)
    while Q:
      x=Q.popleft()
      visited[x]=True
      for y in dic[x]:
        if visited[y]=False:
          Q.append(y)
    ans=0
    ans+=1 if i==True for i in visited
    
 
5 区间加法 [0,0,0,0,0]  leetcode 370
def func():
n=length
        l=[0]*(n+1)
        for list in updates:
            l[list[0]]+=list[2]
            l[list[1]+1]+=-list[2]

        for i in range(1,n+1):
            l[i]+=l[i-1]
        return l[:-1]
6 visiting cities
red=[2,3,4]
blue=[3,1,1]
cost=2
def func(red,blue,c):
  dp=[0]*3
  if red[0]<blue[0]+c:
    dp[0]=red[0]
    blue=False
  else:
    dp[0]=blue[0]+c
    blue=True
  for i in range(1,2):
    
    if blue==False:
      if red[i]<2*c+blue[i]:
        dp[i]=dp[i-1]+red[i]
        blue=False
      else:
        dp[i]=dp[i-1]+2*c+blue[i]
        blue=True
      
    if blue==True:
      if red[i]<blue[i]:
        dp[i]=dp[i-1]+red[i]
        blue=False
      else:
        dp[i]=dp[i-1]+blue[i]
        blue=True
        

动态规划方法
red=[2,3,4]
blue=[3,1,1]
cost=2
def func(red,blue,c):
  dp=[[0,0]*4]
  dp[0]=[0,c]
  for i in range(1,4):
    dp[i][0]=min(dp[i-1][0]+red[i-1],dp[i-1][1]+blue[i-1])
    dp[i][1]=min(dp[i-1][0]+c+red[i-1],dp[i-1][1]+blue[i-1])
  return dp

    
  
  
         
        
    
  
      
    
    
          
          
     
  
   
      
   
      

    
    
    
      
    
  
