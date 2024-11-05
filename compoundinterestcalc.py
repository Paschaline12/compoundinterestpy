#Compound Interest Calculator in Python. For this program we need:

principle = 0 #This is the intial money that has been borrowed.
rate = 0 #This is the rate of interest of borrowing the money
time = 0 # Our time is going to be in years. 

while True:
    principle = float(input("Enter the Principle Amount: "))
    if principle < 0:
        print("The principle amount of money borrowed can not be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("The rate of interest can not be less than Zero")
    else:
        break

while True:
    time = int(input("Enter the period of loan in years: "))
    if time < 0:
        print("The period of the loan can not be less than zero ")
    else:
        break

total = principle * pow((1+rate/100), time)
print(f"Balance after {time} years is: ${total:.2f}")
