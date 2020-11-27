def list_sum(the_list): 
    sum = 0
    for item in the_list: 
        sum += item
    return sum

the_list = [1,4,10]
print("Somma: {}".format(list_sum(the_list)))