### Max profit from  an array of stock price

def maxProfit(arr):
    buy=arr[0]
    sell=arr[0]
    profit=0
    for i in range(0,len(arr)):
        print(i)
        if i+1==len(arr):
            if[arr[i]>sell]:
                sell=arr[i]
                profit+=sell-buy
                return profit
        elif arr[i]>=arr[i+1]:
            sell=arr[i]
            profit+=sell-buy
            buy=arr[i+1]
        elif arr[i]<=buy: 
            buy = arr[i]
        elif arr[i]>sell: 
            sell=arr[i]
    return profit

maxProfit([10,50,60,10,80,10,30,60])