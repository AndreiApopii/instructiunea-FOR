m=int(input("introduceti m:"))
n=int(input("introduceti n:"))
if m%2==0:
    for i in range(m+1,n,2):
        print(i,end=" ")
else:
    for i in range (m,n,2):
        print(i,end=" ")