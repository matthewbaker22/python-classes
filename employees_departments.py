class Employee:
    def __init__(self, first_name, job_title, start_date):
        self.first_name = first_name
        self.job_title = job_title
        self.start_date = start_date

class Company:
    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()
    
    def output(self):
        for employee in self.employees:
            print(f"{employee.first_name} is an employee of {self.business_name}")

nss = Company("Mask", "123 Main St.", "Tech")
vanderbuilt = Company("Vanderbuild School", "456 East St.", "Iron")

employee_1 = Employee("Matt", "Web Developer", "2020-02-22")
employee_2 = Employee("Kyle", "Front End Dev", "2019-07-16")
nss.employees.append(employee_1)
nss.employees.append(employee_2)
nss.output()

print("")

employee_3 = Employee("Jack", "Worker", "Today")
employee_4 = Employee("Frank", "Worker", "Today")
employee_5 = Employee("Lucy", "Worker", "Today")
vanderbuilt.employees.append(employee_3)
vanderbuilt.employees.append(employee_4)
vanderbuilt.employees.append(employee_5)
vanderbuilt.output()