height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI_score=round(weight/height**2)

if BMI_score<19:
  print(f"Your BMI is {BMI_score}, you are underweight.")
elif BMI_score<25:
  print(f"Your BMI is {BMI_score}, you have a normal weight.")
elif BMI_score<30:
  print(f"Your BMI is {BMI_score}, you are slightly overweight.")
elif BMI_score<35:
  print(f"Your BMI is {BMI_score}, you are obese.")
else:
  print(f"Your BMI is {BMI_score}, you are clinically obese.")
