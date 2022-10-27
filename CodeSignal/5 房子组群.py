def func4(l,q):
    def div(l1,num):
        l=0
        r=len(l1)-1
        while l<=r:
            mid=l+(r-l)//2
            if l1[mid]==num:
                return mid
            elif l1[mid]<num:
                l=mid+1
            else:
                r=mid-1
        return mid
        
        
    l.sort()
    i=0
    count=1
    newl=[]
    res=[]
    while i<len(l)-1:
        if l[i+1]==l[i]+1:
            count+=1
        else:
            newl.append(l[i-count+1:i+1])
            count=1
        i+=1
        
    if count>=1:
        newl.append(l[i-count+1:len(l)])
    for num in q:
        for li in newl:
            if num==li[0] or num==li[-1]:
                li.remove(num)
                if li:
                    res.append(len(newl))
                elif not li:
                    newl.remove(li)
                    res.append(len(newl))
            elif li[0]<num<li[-1]:
                idx=div(li,num)
                
                newl.append(li[0:idx])
                newl.append(li[idx+1:len(li)])
                newl.remove(li)
                res.append(len(newl))
                
    return res      
    
