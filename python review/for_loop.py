for i in range(1, 15):
    if i == 13:
        continue  # ignore number 13nd
    else:
        print(i)

print("end coutinue \n")
    
for i in range(1, 15):
    if i == 13:
        pass  # it means notthing but it ignores 13nd
    else:
        print(i)

print("end pass \n")

for i in range(1, 15):
    if i == 13:
        break  # break loop in number 13nd
    else:
        print(i)

print("end break \n")