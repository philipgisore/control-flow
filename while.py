#User input validation:
age = 0

while age < 18:
 age = int(input("Enter your age (must be 18 or older): "))

print("You are old enough to proceed.")



#Guessing Game
secret_number = 7
guess_count = 0
guess = 0

while guess != secret_number:
 guess = int(input("Enter a number between 1 and 10: "))
 guess_count += 1
print(f"You guessed it in {guess_count} tries!")


#iterating until a specific condition
shopping_list = ["apples", "bread", "cheese"]
item_found = False

while not item_found:
 item = input("Search for an item in your list (or 'q' to quit): ")
 if item.lower() == "q":
  break # Exit the loop if the user enters 'q'
 if item in shopping_list:
  item_found = True
  print(f"{item} is in your shopping list.")
 else: 
  print(f"{item} is not on your list.")


#Nested Loops, counting down from 5 with a nested while loop
outer_count = 5

while outer_count > 0:
 #Outer loop controls how many times the inner loop runs
 inner_count = 1
 while inner_count <= outer_count:
  #inner loop repeats for each outer loop iteration
  print(inner_count, end="")
  inner_count += 1
  print() # Move to a new line after each outer loop iteration
  outer_count -= 1

#Printing a multiplication Table
for i in range(1, 11):
 #Outer loop iterates through rows (multiplication factors)
 for j in range(1,11):
  # Inner loop iterates through columns (other factors)
  product = i * j
  print(f"{i} * {j} = {product}", end="\t") # Print with tabs for better formatting
  print() #move to a new line after each row

  #Printing a right Triangle of Asterisks
rows = 5

for i in range(1, rows + 1):
    #outer loop controls the number of rows
    for j in range(1, i + 1):
     #inner loop prints Asterisks for each row
     print("*", end="")
    print()  
   
    
    
   


  