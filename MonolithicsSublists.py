# Monolithic Sublists Input: [1,2,3,4,7,5,6,3,2] output: [[1,2,3,4,7],[5,6],[3],[2]]

def monolithicSublist(arr):
	lst=[arr[0]]
	result=[]
	for i in range(1,len(arr)):
		if arr[i]>arr[i-1]: lst.append(arr[i])
		else:
			result.append(lst)
			lst=[]
			lst.append(arr[i])
	result.append(lst)
	return result


monolithicSublist([1,2,3,4,7,5,6,3,2])