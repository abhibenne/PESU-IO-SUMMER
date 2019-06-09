#Binary search
l = [ 2, 3, 4, 10, 40 ]
ele=2
lv=0
rv=len(l)-1
pos=-1
while rv>=lv:
	mid=(lv+rv)/2
	if ele==l[mid]:
		pos=mid
		break;
	if ele>l[mid]:
		lv=mid+1
	else:
		rv=mid-1
if pos !=-1:
	print("Element found in "+str(pos)+" index")
else:
	print("not found")
