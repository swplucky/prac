def knapSack(bag,weight,profit,n):
    if n==0 or bag==0:
        return 0
    if weight[n-1]>bag:
        return knapSack(bag,weight,profit,n-1)
    else:
        return max(profit[n-1] + knapSack(bag-weight[n-1],weight,profit,n-1),
                   knapSack(bag,weight,profit,n-1))

if __name__ == '__main__':
    bag = 50
    weight = [80,10,30,40]
    profit = [10,4,3,7]
    n = len(weight)
    print(knapSack(bag,weight,profit,n))