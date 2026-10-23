

# # com1

# class Computer:
#     #properties and methods
#     #method
#     def config(self):
#         print("i7, 16GB RAM, 1TB Hard drive")
        
# com1= Computer()
# com2= Computer()

# Computer().config(com1)
# Computer().config(com2)


class Computer:
    # Method
    def __init__(self,cpu,ram,ssd):
        print("init called")
        self.cpu=cpu
        self.ram=ram
        self.ssd=ssd
        
    def config(self):
        print("config: ", self.cpu, self.ram, self.ssd)

# Creating objects (instances) of the class
com1 = Computer("i5", "16GB", "512GB")
com2 = Computer("i9", "96GB", "2TB")
# Calling the method using the class name and passing the object
# Computer.config(com1)
# Computer.config(com2)
com1.config()
com2.config()