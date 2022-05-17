print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15%? "))
people = int(input("No of people? "))
Total_Pay = total + total * tip / 100
Indi_Pay = Total_Pay / people
Indi_Pay_Roundup = round(Indi_Pay , 2)
print( f"The individual payment is {Indi_Pay_Roundup}")

