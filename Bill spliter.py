#input block
Total_bill = float(input("Whats the total bill: "))
Number_of_people = int(input("How many people are there: "))
TiP_percentage = float(input("What is the Tip percentage: "))
Tax_percentage = float(input("What is the Tax percentage: "))

#calculation block
Tip = TiP_percentage / 100 * Total_bill
Tax = Tax_percentage / 100 *Total_bill
Grande_total = Total_bill+Tax+Tip
Share_per_person = Grande_total/Number_of_people

#output
print("The total Tip amounts to: ",Tip)
print("Your total Tax amounts to: ",Tax)
print("each person will need to contribute money amounting to: ",Share_per_person)