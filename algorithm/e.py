x1,y1,x2,y2=map(float,input().split())

Z=(x2-x1)**2+(y2-y1)**2
q=int(input())

for i in range(q):
    x,y=map(float,input().split())
    w=((x-x1)*(x2-x1)+(y-y1)*(y2-y1))/Z
    Mx,My=x1+w*(x2-x1),y1+w*(y2-y1)
    

