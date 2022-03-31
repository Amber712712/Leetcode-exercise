复习偷盗问题（树+动规）+ 比树根节点的第二大问题
复习合并树

1 比树根节点的第二大问题 dfs解法

2 路径问题 找出路径和为定值的路径
注意dfs 和bfs 的不同
BFS
def func(root):
  if not root:
            return []
        res=[]
        q=collections.deque([(root,[root.val],root.val)])
        
        while q:
            n,path,s=q.popleft()
            if not n.left and not n.right:
                if s==targetSum:
                    res.append(path)
            if n.left:
                q.append((n.left,path+[n.left.val],s+n.left.val))
            if n.right:
                q.append((n.right,path+[n.right.val],s+n.right.val))

        return res
      
DFS
def func(root):
   res=[]
        if not root:
            return []
        
        def dfs(node,targetSum,path):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right and node.val==targetSum:
                res.append(path+[node.val])
            dfs(node.left,targetSum-node.val,path+[node.val])
            dfs(node.right,targetSum-node.val,path+[node.val]) 
        
        dfs(root,targetSum,[])
        return res

3 
  

  
  
