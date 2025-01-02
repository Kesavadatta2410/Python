# input = arr[] = {{60,10},{100,20},{120,30}}
#output = 240
# by explaining the terms of weight 10 and 20 kg and 2/3 fraction of 30kg. hence total price will be 60+100+(2/3)(120)=240

def fractional_knapsack(values,weights,W):
    n = len(values)
    #calculate values/weight ratio for each item
    ratios = [(values[i]/weights[i],values[i],weights[i]) for i in range(n)]
    #sort items based on ratio in the non increasing order
    ratios.sort(reverse=True)
    total_value = 0 #initialise total value
    current_value = 0 #initialise current value
    #loop through all items
    for ratio, value, weight in ratios:
        #if the current weight is less than or equal to the given weight limit
        if current_value + weight <= W:
            #add entire item 
            total_value += value
            current_value += weight
        #if the current weight is more than the given weight limit
        else:
            #add fraction of time
            fraction = (W - current_value)/weight
            total_value += fraction * value
            break
    return total_value
#example usage
values = [60,100,120]
weights = [10,20,30]
W1 = 50
print("Maximum value in knapsack is",fractional_knapsack(values,weights,W1))
# output = 240+
values = [40,100,50,60]
weights = [20,10,40,30]
W1= 50
print("Maximum value in knapsack is",fractional_knapsack(values,weights,W1))