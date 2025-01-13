
import employees as emp
import hr
import productivity as prod
import contacts




salary_employee = emp.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = emp.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = emp.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)



manager = emp.Manager(1, 'Marry Poppins', 3000)
manager.address = contacts.Address( '121 Admin Rd', 'Concord', 'NH', '03301')

secretary = emp.Secretary(2, 'John Smith', 1500)
secretary.address = contacts.Address( '67 Paperwork Ave.', 'Manchester', 'NH', '03101')

sales_guy = emp.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worked = emp.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = emp.TemporarySecretary(5, 'Robin Williams', 40, 9)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worked,
    temporary_secretary
]

productivity_system = prod.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)