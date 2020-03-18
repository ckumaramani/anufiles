

Class Employee:
    Company_name="TCS"
    Company_address="HYD"
    def __init__(self,eno,ename,edept,edesg,esal):
        self.employee_no=eno
        self.employee_name=ename
        self.employee_department=edept
        self.employee_designation=edesg
        self.employee_salary=esal
        print("self",id(self))
    def display(self):
        print("COMPANY NAME=",Employee.Company_name)
        print("COMPANY ADDRESS=",Employee.Company_address)
        print("EMPLOYEE ID=",self.employee_no)
        print("EMPLOYEE NAME=",self.employee_name)
        print("EMPLOYEE DEPARTMENT=",self.employee_department)
        print("EMPLOYEE DESIGNATION=",self.employee_department)
        print("EMPLOYEE SALARY=",self.employee_salary)
    e1=Employee(1001,"ravi","SE","IT",100000)
    print("e1",id(e1))
    print("*",*40)
    e2=Employee(1002,"raju","SE","IT",200000)
    print("e2",id(e2))
    e3=Employee(1003,"rajesh","SE","IT",200000)
    print("e3",id(e3))
       

    
    
employee.py
Displaying employee.py.
