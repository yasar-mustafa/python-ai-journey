# conditions (if/else)

name = input("what is your name? ")
hours = float(input("How many hours do you study daily? "))

print("\n--- Perfomance Analysis ---")

if hours >= 4:
    print(f"{name}, you are operating at elite level 🚀")
elif hours >=2:
    print(f"{name}, you are consistent. Keep Pushing 💪")
else:
    print(f"{name}, increase your study time. you can do better 🔥")