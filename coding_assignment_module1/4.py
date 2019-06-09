# Sum of digits of integer
a=1234
b=str(a)
sum=0
for i in b:
	sum+=int(i)
print(sum)

"""
a=1234
sum=0
while a:
    sum+=a%10
    a/=10
print(sum)

"""