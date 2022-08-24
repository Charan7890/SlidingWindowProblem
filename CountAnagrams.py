
string = input().strip()

sub_string = input().strip()

sub_map = {}

for i in sub_string:
	if i in sub_map:
		sub_map[i]+= 1
	else:
		sub_map[i]= 1
count = len(sub_map)
i,j,ans=0,0,0
n = len(string)
ws = len(sub_string)
 # condition for window sliding

 # Base Conditions

if string==sub_string:
	print(1)
elif len(sub_string)>len(string):
	print(0)
else:
	while j<n:
		if string[j] in sub_map:
			sub_map[string[j]]-=1
		if string[j] in sub_map:
			if sub_map[string[j]]==0:
				count-=1

		if j-i+1<ws:
			j+=1
		elif j-i+1==ws:
			if(count==0):
				ans+=1
			if string[i] in sub_map:
				sub_map[string[i]]+=1
			if string[i] in sub_map and sub_map[string[i]]==1:
				count=1
			i+=1
			j+=1
			# print(j)

print("Number of anagrams are:"+str(ans))