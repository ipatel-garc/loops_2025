# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# for loops =executive a block of code a fixed number of times
# You can iterate over a range, string, sequence, etc

for x in reversed(range(1,11,2)):
    print(x)

print("HAPPY NEW YEAR")

for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)

# While loops = execute some code WHILE some condition remains true

name=input("Enter your name?")

if name =="":
    print("You did not enter your name")
    name+input("Enter your name?")
else:
    print(f"Hello {name}")

age= int(input("Enter your age:"))

while age<0:
    print("Age cannot be negative.")
    age= int(input("Enter your age:"))

print(f"You are {age} years old")
