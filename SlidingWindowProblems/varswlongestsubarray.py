arr = list(map(int,input().split(' ')))

n = len(arr)

tot = 3

i,j,sm,mx = 0,0,0,0
try:
	while j<n:
		sm+=arr[j]
		if(sm<tot):
			j+=1

		elif(sm == tot):

			mx=max(mx,j-i+1)

			j+=1

		else:
			while(sm>tot):
				sm-=arr[i]
				i+=1
			j+=1
except:
	pass

print(mx)











	


