##tip calculator
## initial input prompt
total = float(input("Total: \n"))
service = input("How was your service? Good, Fair, Bad?\n")

##  percentages 
good = .20
bad = .10
fair= .15

## calculations
if service == "good":
    tip_total = good * total  
    if service == "fair":
        tip_total = fair * total       
else:
    service == "bad"
    tip_total = bad * total

##final calculation
total_2 = total + tip_total
    

## print statements
print("Total bill amount: %.2f \n" % total)
print("Level of service: %s \n" % service)
print("Tip amount: %.2f \n" % tip_total)
print("Total amount: %.2f \n " %total_2 )