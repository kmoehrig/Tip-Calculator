#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print ("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? "))
tip_percent = float(input("What percent would you like to tip? "))
total_people = float(input("How many people are you splitting the bill with? "))

tip = total_bill*(tip_percent/100)

ind_total = (total_bill+tip)/total_people

final_amount = "{:.2f}".format(ind_total)
print(f"Each person should pay ${final_amount}")