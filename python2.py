print('Starting Python tutorial')

class student:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    def addi(self):
        return(self.val1+self.val2)

stu1 = student(5,5)
print(stu1.addi())
print("This is over")
