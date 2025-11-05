def simple_interest(p,t,senoir):
    rate = 12 if senior else 10
    interest = (p*t*rate)/100
    return interest
p = float(input("Enter principle amount :"))
t = float(input("Enter time(in year) :"))
senior_input = input("Is the customer a senoir citizen (yes/no)?").lower()
senior = senior_input = "yes"
si =simple_interest(p,t,senior)
print("Simple Interest =",si)
