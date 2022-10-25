def func(m):
  l=[(1,0),(0,1),(1,2),(2,1),(0,2),(2,0)]
  r=len(m)
  s=r//2
  ans=r*r
  for x,y in l:
    res=0
    for i in range(r):
      for j in range(r):
        if i<=s:
          if i==j:
            if m[i][j]!=x:
              res+=1
          elif j==r-1-i:
            if m[i][j]!=x:
              res+=1
          else:
            if m[i][j]!=y:
              res+=1
        else:
          if j==s:
            if m[i][j]!=x:
              res+=1
          else:
            if m[i][j]!=y:
              res+=1
     ans=min(ans,res)
    
 return ans
              
          
        
    
