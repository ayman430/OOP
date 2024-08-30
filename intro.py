#create class 
class Employee:
    # class attribute: cant use it without class name to use it -> class_name.class_attribute  
    num_of_emps = 0

    # create constructor: first thing object see after creating it 
    def __init__(self, name, age, salary):
        #Object Atrributes
        self.name = name
        self.age = age
        self.salary = salary
        #increment num_of_emps each time object created 
        Employee.num_of_emps += 1

    # create instance(object) method
    def update_salary(self, new_salary):
        self.salary = new_salary

    # create class method -> use classmethod decorator
    @classmethod
    def class_method(cls):
        return 'This is a class method'

    # create static method -> free method can use it at any place by any way 
    @staticmethod
    def hi():
        return 'Hi from static method'



# create objects
# emp1 = Employee('ayman', 23, 2000)
# print(f'Employee name is: {emp1.name} and age: {emp1.age}')
# print(f'Number of employees: {Employee.num_of_emps}')

emp2 = Employee('ali', 18, 2000)
print(f'Employee name is: {emp2.name} and age: {emp2.age}')
print(f'Number of employees: {Employee.num_of_emps}')
print(f'employee salary: {emp2.salary}')
emp2.update_salary(4000)
print(f'employee new salary: {emp2.salary}')
print(Employee.class_method())
print(Employee.hi())


