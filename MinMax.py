## Delete Min Max using single loop

def removeMinMax(arr):
    index = []
    min = max = arr[0]
    for i in range(len(arr)):
	    if arr[i]<min:
	        min = a[i]
	    elif arr[i]>max:
	        max = arr[i]
    for i in range(len(arr)):
        if arr[i] == min or arr[i] == max:
	        index.append(arr[i])
    for i in index:
        arr.remove(i)
    print(arr)
            
	 
arr = [1,2,3,4,5,1,5,1,7,9,9]

removeMinMax(arr)
