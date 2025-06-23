#Checking Eligibility to vote based on age with if and else
age = int(input("Enter your age:"))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#Discount Calculator with elif
purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount >= 1000:
    discount = 0.1 #10%discount
elif purchase_amount >=500:
    discount = 0.05 #5% discount
else:
    discount = 0 #No discount

final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))

#letter Grade Assigner with Nested if Statements
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >=70:
    grade = "C"
else:
    grade = "F"

print("Your grade is: ", grade)
