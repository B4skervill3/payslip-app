import GrossSalary as GS
import NetSalary as NS
import SalaryDeductions as SD


print("\nPayslip App")

name = input("\nEnter name here: ",)
hours = int(input("Enter total hours: "))
loan = float(input("Enter amount of desired Loan: "))
insurance = float(input("Enter health insurance: "))

print("\nEmployee Payslip Details")
print("Name: ", name)
print("Hours: ", hours)
print("Gross Salary: ", GS.gross_salary(hours))

print("\nTotal Salary Deductions: ")
tax_deduction = SD.tax_deduction(GS.gross_salary(hours))
print("Tax: ", tax_deduction)
print("Loan: ", loan)
print("Insurance: ", insurance)

print("Total Deductions: ", NS.total_deductions(tax_deduction, loan, insurance))

net_salary = NS.net_salary(GS.gross_salary(hours), NS.total_deductions(tax_deduction, loan, insurance))
print("\nNet Salary: ", net_salary)
