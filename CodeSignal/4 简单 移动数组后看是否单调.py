def func(l):
  newl=l+l
  count=1
  i=0
  while i<len(newl)-1:
    if newl[i+1]<newl[i]:
      count+=1
      
      if count==len(l):
        return len(newl)-1-i-1
      
    else:
      count=1
    i+=1
 
  return -1
   
