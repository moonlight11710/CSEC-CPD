a,b=map(int,input().split())
year=0
while a<=b:
    a=a*3
    b=b*2
    year+=1
else:
    print(year)
