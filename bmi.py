height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {round(bmi, 1)}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")

