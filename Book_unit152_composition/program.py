import json
from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees import employee_database, Employee

def print_dict(d): 
    print(json.dumps(d, indent=2))

employees = employee_database.employees

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)
temp_secretary = Employee(5)

print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())

