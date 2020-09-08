# #%%
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
# class Employee(Person):
#     all_employees = []
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname, lname)
#         self.empid = empid
#         Employee.all_employees.append(self)

# p1 = Person('George', 'smith')
# print(p1.fname, '-', p1.lname)
# e1 = Employee('Jack', 'simmons', 456342)
# e2 = Employee('John', 'williams', 123656)
# print(e1.fname, '-', e1.empid)
# print(e2.fname, '-', e2.empid)
# #%%
# print(Person.__mro__)


# #%%
# class Employee(Person):
#     all_employees = EmployeesList()
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname, lname)
#         self.empid = empid
#         Employee.all_employees.append(self)
#     def getSalary(self):
#         return 'You get Monthly salary.'
#     def getBonus(self):
#         return 'You are eligible for Bonus.'

# class ContractEmployee(Employee):
#     def getSalary(self):
#         return 'You will not get Salary from Organization.'
#     def getBonus(self):
#         return 'You are not eligible for Bonus.'
# e1 = Employee('Jack', 'simmons', 456342)
# e2 = ContractEmployee('John', 'williams', 123656)
# print(e1.getBonus())
# print(e2.getBonus())
# #%%



# #%%
# # Private attribute example
# class Employee(Person):
#     all_employees = EmployeesList()
#     def __init__(self, fname, lname, empid):
#         Person.__init__(self, fname, lname)
#         self.__empid = empid
#         Employee.all_employees.append(self)
#     def getEmpid(self):
#         return self.__empid

# e1 = Employee('Jack', 'simmons', 456342)
# print(e1.fname, e1.lname)
# print(e1.getEmpid())
# print(e1.__empid)

# #%%
# class A:
#     x = 0

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         A.x += 1

#     def __init__(self):
#         A.x += 1

#     def displayCount(self):
#         print('Count : %d' % A.x)

#     def display(self):
#         print('a :', self.a, ' b :', self.b)

# a1 = A('George', 25000)
# a2 = A('John', 30000)
# a3 = A()
# a1.display()
# a2.display()
# print(A.x)
# %%
class A:
    def __init__(self, a = 5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)
# %%
