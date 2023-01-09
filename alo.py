num=int(input("enter the number"))

for i in range(1,11):
    print(num,'x',i,'=',num*i)

pr=int(input("enter the number for the prime :"))

for i in range (2,int(pr/2)+1):
    if(pr%i==0):
        print(" it is not prime")
        print(i,'times',pr//i,'is',pr)
        break
    else:
        print("it is a prime number")


num2=int(input("enter the number :"))
fact =1
for i in range(1,num2+1):
    fact=fact*i

print(fact)
