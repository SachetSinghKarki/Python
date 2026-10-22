

def square(num):
    return num * num
    
def cube(num):
    return num * num * num

def operate(num, operation):
    
    return operation(num)
    
value = int(input("Enter a number: "))
result = operate(value,cube)
print(result)