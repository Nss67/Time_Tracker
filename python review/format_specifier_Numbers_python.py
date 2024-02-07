x = 200025500.987654231
y = 36566.2154
z = -5565.247123

# decimal point decission 0.000
print(f"your number is {x:.4f}")
print(f"your number is {y:.3f}")
print(f"your number is {z:.2f}")

# spacing
print(f"your number is {x:>50}")  # last 50 character
print(f"your number is {y:^50}")  # middle 50 character
print(f"your number is {z:<50}")  # first 50 character
print()
print(f"your number is {x:,}")
print(f"your number is {y:+}")
print(f"your number is {z: }")
print()
print(f"your number is {x:,.2f}")
print(f"your number is {y:+,.2f}")
print(f"your number is {z: ,.2f}")
