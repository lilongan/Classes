## initial statement and user input
print("You have 0 coins.")

##counter
coins_collected = 0

##input loop (using 10 just as a tester, would write differntly for unknown user count limit)
for coins_collected in range(0,10):
    coins_desired = input("Do you want another?")
    if coins_desired == "yes":
        coins_collected += 1
        print(f"You have {coins_collected}")
    else:
        break 