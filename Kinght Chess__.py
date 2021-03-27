"""
All submissions for this problem are available.
Simran got bored of 8x8 chess board and invented the new variation of Chess, the one on an infinite chess board. 
There is only a white king and N black knights. The white king has to avoid checkmate as long as it can.
A situation is given. Determine if white king is in checkmate or not. The white king is in checkmate if and only if it is in check 
and it is not able to move to any of its neighboring positions which is not in check.
"""

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for k in range(n):
        x,y=map(int,input().split())
        arr.append([x+2,y+1])
        arr.append([x+2,y-1])
        arr.append([x-2,y+1])
        arr.append([x-2,y-1])
        arr.append([x+1,y+2])
        arr.append([x-1,y+2])
        arr.append([x+1,y-2])
        arr.append([x-1,y-2])
    king=[]    
    a,b=map(int,input().split())
    king.append([x,y+1])
    king.append([x,y-1])
    king.append([x+1,y])
    king.append([x-1,y])
    king.append([x+1,y+1])
    king.append([x+1,y-1])
    king.append([x-1,y+1])
    king.append([x-1,y-1])
    ans=1
    for kp in king:
        for j in arr:
            if kp==j:
                ans=0
                break
    if ans:
        print("NO")
    else:
        print("YES")