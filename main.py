from datetime import datetime, date
# welcome to program
print("Hello and Welcome to your Time Tracker")
# make user profile if it is new


# inputs and questions
course = input("what do you want to learn or practice? ")
pause_times = []
total = None
result = None
while True:
    ready = input("\nAre you ready? (default is Y) ")

    # conditions and record start time, break time, end time
    if ready == "":
        ready = "Y"
    if ready.upper()[0] == "Y":
        dt1 = datetime.now()

        pause = input(f"""\nyou start in {dt1.ctime()}.
        if you want to pause break press Enter or C to cancel this step: """)

        if pause.upper() != "C":
            dt2 = datetime.now()
            dtp = dt2 - dt1
            print(dtp)
            pause_times.append(dtp)
        else:
            pass
    else:
        for i in pause_times:
            if total is None:
                total = i
            else:
                total += i

        print(f"\ntotal of your today practice of the {course} is {total} that was so good:)")
        result = total
        total = None

        exit1 = input(f"\nif you want to exit press E or C to continue: (default is E) ")
        if exit1 == "":
            exit1 = "E"
        if exit1.upper()[0] == "E":
            with open("records.txt", mode="a") as file:
                file.write(f"{date.today()} {course} {result}\n")
                file.close()
            break

# save all values in a file (txt, spreadsheet, database) and configure them

# GUI with kivy

# Tag

# Timer2

# finally I could connect to GitHub


