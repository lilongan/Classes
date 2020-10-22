##initial user input
height = int(input("Enter height: \n"))
width = int(input("Enter width: \n"))

##formula for string print out
row_1 = width * "*"
space = "*" + " " * (width - 2) + "*"

##box print
print(row_1 + "\n" + (space + "\n")*(height) + row_1)