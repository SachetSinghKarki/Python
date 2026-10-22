from functools import reduce

nums = [1,2,3,4,5,6,7]


# for i in nums:
#     if i%2==0:
#         evens.append(i)

# def is_even(n):
#     return n%2 == 0

# def double_it(n):
#     return n *2

# def sum_it(a,b):
#     return a+b

sum_it = lambda a,b: a+b
    
double_it = lambda n: n *2
is_even = lambda n: n%2==0
evens = list(filter(is_even, nums))
doubles = list(map(double_it, evens))
total = reduce(sum_it, doubles)
print(evens)
print(doubles)
print(total)