import json
import os

# Enter your height in meters
height = float (input ("Enter your height in meters (e.g. 1.65): "))

# Enter your weight in kg
weight = float (input (" Enter your weight in kg (e.g. 55): "))

#Calculate BMI
BMI = weight / (height * height)

#Show the results
print (f"Your BMI is {BMI: .1f}")

#Explain the results
if BMI < 18.5:
 category = "underweight"
 print (" You are underweight")
elif BMI <25:
 category = "normal"
 print ("You are at normal weight")
elif BMI <30:
 category = "overweight"
 print ("You are overweight")
else:
 category = "obese"
 print ("Obese")

# Save the results to a JSON file
record = {
    "height": height,
    "weight": weight,
    "BMI": round(BMI, 1),
    "category": category
}

file_path = "bmi_records.json"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        records = json.load(f)

else:
    records = []

records.append(record)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4)

print(f"\n Record saved! Total records: {len(records)}")