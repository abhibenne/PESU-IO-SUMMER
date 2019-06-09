# String is numeric
a="1097654372"
if str.isdigit(a):
	print("numeric")
else:
	print("not numeric")


# String is numeric and number of integers and charachters
a="109765"
ch=0
inte=0
for i in a:
    if str.isdigit(i):
        inte+=1
    else:
        ch+=1
print(inte)
print(ch)