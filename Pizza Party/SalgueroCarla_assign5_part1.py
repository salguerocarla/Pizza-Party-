'''
Carla Salguero

#need to validat ethe number of slices each person gets.
#users will always enter numbers
#cant do comma in an input, but can do plus
'''
#Part 1: Pizza Party

#Here just sets up some user input values. 
budget = float(input("Enter the budget for your party: "))
cost_per_slice = float(input("Cost per slice of pizza: "))
cost_wholepizza = float (input("Cost per whole pizza pie (8 slices): "))
people = int(input("How many people will be attending your party? "))


slice = 0 #here sets up an accumulator value.     
for i in range (1,people+1): #this sets up the range to be from one person to people +1. 
    while True:
        question = "Enter number of slices for person #"+ str(i)+":" #a way to combine the string with an integer (which we changed to a string).
        slices = int(input(question)) #inputs the variable above. 
        if slices <=0:
            print ("Not a vlaid entry, try again!")
        else:
            break
    slice += slices

#slice has the total amount of slices that is needed.
pie = slice // 8
slice_left = (slice % 8)

        
total_cost = (pie* cost_wholepizza) +(cost_per_slice * slice_left)
while True:
    if budget < total_cost:
        print ("Your order cannot be completed")
        print ("You would need to purchase", pie, "pies and ", slice_left, "slices")
        break
    else:
        print ("You should purchase", pie, "pies and", slice_left, "slices")
        print ("Your total cost will be:", format(total_cost,".2f"))
        break

             
left_over_money = budget - total_cost
if left_over_money ==0:
    print ("You will have no money left after your order.")
elif left_over_money < 0:
    left_over_money = left_over_money * -1
    print ("This would put you over budget by", format(left_over_money,".2f"))
else:
    print ("You will still have", format(left_over_money,".2f")," left after your order.")
             

