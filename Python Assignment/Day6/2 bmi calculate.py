


def calculate_bmi(weight,height):
    # weight = float(input("Enter your weight (kg) : "))
    # height = float(input("Enter your height  (m)  : "))
    bmi = weight / (height ** 2)
    if bmi < 18.5 :
        category = "Underweight"
    elif bmi > 18.5 and bmi < 24.9 :
        category = "Normal"
    elif bmi > 25 and bmi < 29.9 :
        category = "Overweight"
    else : #bmi > 30  : 
        category = "Obese"
    return round(bmi, 2), category
    
print(f" BMI : {bmi} " )
print(f" Category : {category} " )
    

weight = float(input("Enter your weight (kg) : "))
height = float(input("Enter your height  (m)  : "))

calculate_bmi(weight,height)

