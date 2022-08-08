
arr = list(map(int,input().split(' ')))

n = len(arr)

k = int(input())

i,j,l = 0,0,[]

while j<n:
	if(arr[j]<0):
		l.append(arr[j])
	if j-i+1 < k:
		j+=1
	elif j-i+1 == k:
		if(l == []):
			print(0)
		else:
			print(l[0])
			if(arr[i]==l[0]):
				l.pop(0)
		i+=1
		j+=1

