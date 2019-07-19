print("Please input the following values to get your BMI result")
weight= float(input("Please type in your weight in kg: "))
height= float(input("Please type in your height in m: "))
bmi = weight/(height**2)
bmi = round(bmi, 1)
print("Your BMI is ", bmi, "kg/msq")
if (bmi<=0) or (bmi>=100):
    print("Invalid result")
elif (bmi>0) and(bmi<18.5):
    print("You are underweight")
elif (bmi>=18.5) and (bmi<24):
    print("Congratulations! You have a healthy weight")
elif (bmi>=25) and (bmi<30):
    print("You are overweight")
if (bmi>=30):
    print("You are obese")
