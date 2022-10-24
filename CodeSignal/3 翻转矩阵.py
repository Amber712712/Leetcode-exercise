水平线翻转
def fun(matrix):
  n=len(matrix)
  for i in range(n//2):
    for j in range(n):
      matrix[i][j],matrix[n-1-i][j]=matrix[n-1-i][j],matrix[i][j]
      
主对角线翻转
def func(m):
  n=len(m)
  for i in range(n):
    for j in range(i):
      m[i][j],m[j][i]=m[j][i],m[i][j]
此对角线翻转
n=len(m)
for i in range(n-1):
  for j in range(n-1-i):
    m[i][j],m[n-1-j][n-1-i]=m[n-1-j][n-1-i],m[i][j]
    
    
