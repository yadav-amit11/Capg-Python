def happynum(num):
    while True:
        if num==1:
            return True
        elif num==4:
            return False
        s=str(num)
        sum=0
        for i in s:
            sum+=int(i)**2
        num=sum        
n=int(input())
print(happynum(n))