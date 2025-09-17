basic_pay = float(input("Enter the basic pay of the employee :"))
hra = 0.10 * basic_pay
ta = 0.05 * basic_pay
salary = basic_pay + hra +ta
print("Basic pay : ",basic_pay)
print("HRA : ",hra)
print("TA : ",ta)
print("Total salary : ",salary)

