print("FACTOR A NUMBER\n____________\n")

##initial user input
num = int(input("Enter a number: \n\n"))



for i in range(1, num + 1):
    if num % i == 0:
        print(i)