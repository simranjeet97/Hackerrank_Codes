"""
All submissions for this problem are available.
Simran got bored of 8x8 chess board and invented the new variation of Chess, the one on an infinite chess board. 
There is only a white king and N black knights. The white king has to avoid checkmate as long as it can.
A situation is given. Determine if white king is in checkmate or not. The white king is in checkmate if and only if it is in check 
and it is not able to move to any of its neighboring positions which is not in check.
"""

def search(ar,x,y):
   a1=[x-1,y+2]
   a2=[x+1,y+2]
   a3=[x-1,y-2]
   a4=[x+1,y-2]
   a5=[x-2,y+1]
   a6=[x-2,y-1]
   a7=[x+2,y+1]
   a8=[x+2,y-1]
   
   if a1 in ar or a2 in ar or a3 in ar or a4 in ar or a5 in ar or a6 in ar or a7 in ar or a8 in ar:
      return 0
   else:
      return 1

test=int(input())
while test:
   ar=[]
   f=1
   n=int(input())
   while n:
      x1,y1=map(int, input().split())
      ar.append([x1,y1])
      n-=1
   x,y=map(int, input().split())
   
   if search(ar,x,y):
      f=0
   elif search(ar,x-1,y):
      f=0
   elif search(ar,x+1,y):
      f=0
   elif search(ar,x,y-1):
     f=0
   elif search(ar,x,y+1):
      f=0
   elif search(ar,x-1,y-1):
      f=0
   elif search(ar,x+1,y+1):
      f=0
   elif search(ar,x-1,y+1):
      f=0
   elif search(ar,x+1,y-1): 
      f=0
      
      
   if f==1:
      print("YES") 
   else:print("NO")
   test-=1