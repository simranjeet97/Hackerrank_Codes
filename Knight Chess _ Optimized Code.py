for l in range(0,int(input())):
    N=int(input())
    d=[]
    for i in range(0,N):
        d.append(list(map(int,input().split())))
    x,y=map(int,input().split())

    kingpos=[[x-1,y+1],[x-1,y],[x-1,y-1],[x,y+1],[x,y-1],[x+1,y+1],[x+1,y],[x+1,y-1]]
    c=0
    for king in d:
        for knight in kingpos:
            xdiff=abs(knight[0]-king[0])
            ydiff=abs(knight[1]-king[1])
            if (xdiff==1 and ydiff==2) or (xdiff==2 and ydiff==1):
                c+=1
            elif c==7:
                break
        
    if c!=7:
        print("NO")
    elif c==7:
        print("YES")
                   