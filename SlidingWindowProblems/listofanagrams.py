string = list(input())

n = len(string)

sub_str = list(input())

k = len(sub_str)

map_sub_str = {}

dup_sub_str = set(sub_str)

count = len(map_sub_str)

# for i in dup_sub_str:
# 	map_sub_str[i]=sub_str.count(i)

while j<n:
	map_sub_str[a[j]]+=1
	if j-i+1 < k:
		j+=1
	elif j-i+1 == k:
		if(map_sub_str[a[j]]==0):
			count -=1
		i+=1
		j+=1
print(count)