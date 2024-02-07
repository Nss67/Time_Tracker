import time

my_time = int(input("Enter your time in second: "))

for i in range(my_time, 0, -1):
    second = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours}:{minutes}:{second:02}")
    time.sleep(1)

print("Time's up")