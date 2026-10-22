# # # def add(x=0,y=0): #def arg
# # #     return x + y

# # def add(a,*b):
    
# #     sum = a
# #     for n in b:
# #         sum+=n
# #     # print(a)
# #     # print(b)
# #     return sum


# # result = add(1,2,3,4)
# # print(result)
    
    
# def person(name, age = 18):
#     print(f"name: {name}, age: {age}")

# # person("Leo", 19)
# person(age=19, name="Leo") #keyword arguments
    
    
def person (name, **kwargs):
    print(f"Name: {name}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
    
person(name="Leo", age = 19, loc="London", tech="Python")