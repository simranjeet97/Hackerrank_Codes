"""
Formally, given a wall of infinite height, initially unpainted. There occur N operations, and in ith operation, 
the wall is painted upto height Hi with color Ci. Suppose in jth operation (j>i) wall is painted upto height Hj with 
color Cj such that Hj >= Hi, the Cith color on the wall is hidden. At the end of N operations, you have to find the number 
of distinct colors(>=1) visible on the wall.

Help him find out the number of distinct colors on the wall.
"""

def main():
    for i in range(0,int(input())):
        n,m=list(map(int,input().split()))
        h=list(map(int,input().split()))
        c=list(map(int,input().split()))
        j=h.index(max(h))
        h=h[j:]
        c=c[j:]
        index=[]
        new_c=[]
        for j in range(0,len(h)):
            for k in range(j+1,len(h)):
                if h[j]<=h[k]:
                    break
            else:
                    new_c.append(c[j])
        print(len(list(set(new_c))))
        
                
            
if __name__=="__main__":
    main()