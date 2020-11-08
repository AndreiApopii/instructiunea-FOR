a=int(input("introdu a:"))
s=0
for i in range(1,a):
    if((i%3==0)or(i%5==0)):
        s=s=i
print("suma numerelor care se impart la 3 si 5 de la 1 la",a,"este",s)