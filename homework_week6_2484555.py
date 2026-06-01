# ============================================
# TASK 1 — Basic If Statements
# ============================================
# Ask the user for a temperature and respond based on ranges.

# TODO: Write your code here

temp = float(input("Enter the temperature (°C): "))

if temp < 0:
    print("It's freezing! ❄️")
elif temp < 20:
    print("It's a bit cold.")
elif temp < 30:
    print("The weather is nice. 🙂")
else:
    print("It's hot outside! 🔥")
# ============================================
# TASK 2 — Weekday or Weekend?
# ============================================
# Ask user for number 1–7 and print if it's weekday or weekend.

# TODO: Write your code here

day = int(input("Enter a number (1–7): "))

if day == 6 or day == 7:
    print("It's weekend! 🎉")
elif 1 <= day <= 5:
    print("It's a weekday.")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
# ============================================
# TASK 3 — For Loop Practice
# ============================================
# Print all even numbers from 0 to 20 using a loop.

# TODO: Write your code here

for i in range(0, 21):
    if i % 2 == 0:
        print(i)
# ============================================
# TASK 4 — While Loop Practice
# ============================================
# Repeatedly ask the user for a password until correct.

# TODO: Write your code here

correct_password = "python123"

password = input("Enter password: ")

while password != correct_password:
    print("Wrong password, try again.")
    password = input("Enter password: ")

print("Access granted! ✅")
# ============================================
# TASK 5 — break / continue
# ============================================
# Print numbers 1–10
# Skip 5 using continue
# Stop loop at 8 using break

# TODO: Write your code here

for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    if i == 8:
        break      # stop at 8
    print(i)
# ============================================
# TASK 6 — Combined Mini Exercise
# ============================================
# Ask the user for 5 numbers.
# Count positives, negatives, zeros.

# TODO: Write your code here

positives = 0
negatives = 0
zeros = 0

for i in range(5):
    n = float(input(f"Enter number {i+1}: "))

    if n > 0:
        positives += 1
    elif n < 0:
        negatives += 1
    else:
        zeros += 1

print("Positives:", positives)
print("Negatives:", negatives)
print("Zeros:", zeros)
