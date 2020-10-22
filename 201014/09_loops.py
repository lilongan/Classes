# 201014 Class lecture begin

i = 0

while i < 10:
    print(i)
    i = i + 1 #i = i + 1 <--same thing


i = 5
max_num = 10

while i < max_num:
    print(i)
    i += increment

i = 2
max_num = 120

while i < max_num:
    print(i)
    i += i

#   # Note: Stop infinite intiger loop by Ctrl C for Keyboard Interrupt
#   # Note: String loops useful and stopped by an input choice.







#201014 Lesson how-do-i-repeat-a-piece-of-code-over-and-over

donuts_consumed = 0
print("You have eaten %d donuts." % donuts_consumed)
donuts_consumed = donuts_consumed + 1
print("You have eaten %d donuts." % donuts_consumed)
donuts_consumed = donuts_consumed + 1
print("You have eaten %d donuts." % donuts_consumed)
donuts_consumed = donuts_consumed + 1
print("You have eaten %d donuts." % donuts_consumed

donuts_consumed = 0
print("You have eaten %d donuts." % donuts_consumed)
donuts_consumed += 1
print("You have eaten %d donuts." % donuts_consumed)
donuts_consumed += 1
print("You have eaten %d donuts." % donuts_consumed)
donuts_consumed += 1
print("You have eaten %d donuts." % donuts_consumed)

donuts_consumed = 0
while (donuts_consumed < 4):
    print("You have eaten %d donuts." % donuts_consumed)
    donuts_consumed = donuts_consumed + 1

    count = 0
MAX = 10
while (count < MAX):
    print(count)
    count += 1

    count = 0
MAX = 10
while (count < MAX):
    if count < MAX/2:
        print("%d is below the halfway point" % count)
    elif count == MAX/2:
        print("%d is at the halfway point" % count)
    else:
        print("%d is above the halfway point" % count)
        
    count += 1

    count = 0
input_string = input("How high should we count? ")
MAX = int(input_string)
while (count < MAX):
    print(count)        
    count += 1

    count = 0
input_string = input("How high should we count? ")
try:
    MAX = int(input_string)
    while (count < MAX):
        print(count)        
        count += 1    
except ValueError:
    print("Please run the program again and type a number!")

    count = 0
input_string = input("How high should we count? ")
try:
    MAX = int(input_string)
    while (count < MAX):
        is_even = count % 2 == 0
        if is_even:
            print(count)        
        count += 1    
except ValueError:
    print("Please run the program again and type a number!")

    count = 0
input_string = input("How high should we count? ")
try:
    MAX = int(input_string)
    while (count < MAX):
        is_odd = count % 2 != 0
        if is_odd:
            print(count)        
        count += 1    
except ValueError:
    print("Please run the program again and type a number!")

