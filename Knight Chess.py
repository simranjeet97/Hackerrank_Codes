"""
All submissions for this problem are available.
Simran got bored of 8x8 chess board and invented the new variation of Chess, the one on an infinite chess board. 
There is only a white king and N black knights. The white king has to avoid checkmate as long as it can.
A situation is given. Determine if white king is in checkmate or not. The white king is in checkmate if and only if it is in check 
and it is not able to move to any of its neighboring positions which is not in check.
"""

for i in range(int(input())):
    N=int(input())
    x=[0]*N
    y=[0]*N
    
    
    flag=0
    for i in range(N):
        x[i],y[i]=map(int,input().split())
    A,B=map(int,input().split())
    Y=set([(A-1,B),(A+1,B),(A,B+1),(A,B-1),(A-1,B-1),(A-1,B+1),(A+1,B-1),(A+1,B+1)])
    Z=[]
    for i in range(N):
        a=x[i]
        b=y[i]
        X=[]
        X.append((a-2,b-1))
        X.append((a-2,b+1))
        X.append((a+2,b-1))
        X.append((a+2,b+1))
        X.append((a-1,b-2))
        X.append((a-1,b+2))
        X.append((a+1,b-2))
        X.append((a+1,b+2))
        X=set(X)
        if len(Y-X)!=8:
            S=set(Y-X)
            S1=Y-S
            #print(type(Y-S))
            for i in S1:
                if i not in Z:
                    Z.append(i)
        if (A,B) in X:
            flag=1
    #Z=set(Z)
    if flag==0:
        print("NO")
    else:
        #print(Z)
        if len(Z)==8:
            print("YES")
        else:
            print("NO")