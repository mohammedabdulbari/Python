
class Employee:

    employee_count = 101

    def __init__(self, name, desig, sal):
        self.name = name
        self.designation = desig
        self.salary = sal
        self.eid = 'e' + str(Employee.employee_count)
        Employee.employee_count += 1

    def show_details(self):
        print('Name:',self.name)
        print('Eid:',self.eid)
        print('Designation:',self.designation)
        print('Salary:',self.salary)

    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101


e1 = Employee('John', 'Manager', 10000)
e2 = Employee('Mark', 'Team Leader', 8000)

e1.show_details()
print('')
e2.show_details()
print('Total Employees:', e1.total_emp())