n=int(input())
m=int(input())
count_divisible=0
count_not_divisible=0
for i in range(1,m+1):
        if(i%n!=0):
            count_not_divisible +=1
        else:
            count_divisible +=1
print(abs(count_divisible -count_not_divisible))