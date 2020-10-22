day_num = int(input("How many days into this week are we? Enter 0-6\n"))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day_num < 6:
    print("Go to work.")
else:
    print("Sleep in.")