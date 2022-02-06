# COVARIANCE OF TWO SET OF VALUES

# INPUTTING VALUES
a = []
b = []

n  = int(input("Enter number of values in the first list : "))
for i in range(0,n):
    ele = int(input())
    a.append(ele)

m = int(input("Enter number of values in the second list : "))
for j in range(0,m):
    ele = int(input())
    b.append(ele)

# FUNCTION
def covar(num_list_a, num_list_b):
# SUM AND MEAN
    sum_list_a = sum(num_list_a)
    mean_list_a = sum_list_a / len(num_list_a)
    sum_list_b = sum(num_list_b)
    mean_list_b = sum_list_b / len(num_list_b)

# CHECKING IF LENGTH OF TWO LISTS MATCH 
    if len(num_list_a) == len(num_list_b):
# COVARIANCE ENGINE
        lst = []
        list1 = []
        for i in num_list_a:
            value = i - mean_list_a
            list1.append(value)
        list2 = []
        for j in num_list_b:
            value = j - mean_list_b
            list2.append(value)
        mul_list = [u*v for u,v in zip(list1,list2)]
        covariance_value = sum(mul_list)/len(num_list_a)
        return "Covariance = ", covariance_value
    else:
        return "The size of the lists do not match"
                
print(covar(a,b))
