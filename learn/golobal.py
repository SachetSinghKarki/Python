a = 10 #global variable

def smth():
#    print( globals())
   globals()['a'] = 11
   a = 15 #local variable
   print(f"inside{a}")

smth()
print(f"outside{a}")