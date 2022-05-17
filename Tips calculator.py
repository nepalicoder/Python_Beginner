#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15%? "))
people = int(input("No of people? "))
Total_Pay = total + total * tip / 100
Indi_Pay = Total_Pay / people
Indi_Pay_Roundup = round(Indi_Pay , 2)
print( f"The individual payment is {Indi_Pay_Roundup}")

