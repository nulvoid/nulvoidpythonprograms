#to do
#suit and helmet color randomization
#number color and font randomization
import os
import random
import json
import uuid
import requests

car_class = input("Late Model or Super Late Model: ")
folder_name = input("Enter roster name: ")
total_cars = int(input("Enter the number of cars desired for roster: "))

response = requests.get("https://raw.githubusercontent.com/nulvoid/nulvoidpythonprograms/main/first_names.txt")
first_names = response.text.splitlines()
response = requests.get("https://raw.githubusercontent.com/nulvoid/nulvoidpythonprograms/main/last_names.txt")
last_names = response.text.splitlines()
    
def generate_ratings(skill_level):
    if skill_level == "High":
        skill = random.randint(75, 100)
        aggression = random.randint(50, 90)
        optimism = random.randint(75, 100)
        smoothness = random.randint(75, 100)
    elif skill_level == "Medium":
        skill = random.randint(40, 75)
        aggression = random.randint(40, 60)
        optimism = random.randint(60, 75)
        smoothness = random.randint(40, 65)
    else:
        skill = random.randint(0, 40)
        aggression = random.randint(20, 80)
        optimism = random.randint(0, 50)
        smoothness = random.randint(0, 35)
    return skill, aggression, optimism, smoothness

drivers = []
used_car_numbers = []

for i in range(total_cars):
    if car_class == "Late Models":
        car_id = 164
        car_path = "latemodel2023"
        sponsor1_range = [0, 225, 226, 227, 228, 229, 230, 231, 232]
        car_scheme_range = range(1, 25)
    else:  # assume "Super Late Models"
        car_id = 54
        car_path = "superlatemodel"
        sponsor1_range = [0, 111, 112, 113, 114, 115]
        car_scheme_range = range(0, 24)
    car_number = random.randint(0, 99)
    while car_number in used_car_numbers:
        car_number = random.randint(0, 99)
    used_car_numbers.append(car_number)
    skill_level = random.choice(["High", "Medium", "Low"])
    skill, aggression, optimism, smoothness = generate_ratings(skill_level)
    age = random.randint(13, 90)
    pit_crew_skill = random.randint(0, 100)
    pit_strategy_riskiness = random.randint(0, 100)
    first_name, last_name = random.choice(first_names), random.choice(last_names)
    sponsor1 = random.choice(sponsor1_range)
    car_scheme = random.choice(car_scheme_range)
    color1 = '%06x' % random.randint(0, 0xFFFFFF)
    color2 = '%06x' % random.randint(0, 0xFFFFFF)
    color3 = '%06x' % random.randint(0, 0xFFFFFF)
    car_design = f"{car_scheme},{color1},{color2},{color3}"

    driver = {
        "driverName": f"{first_name} {last_name}",
        "carNumber": f"{car_number:02d}",
        "carDesign": car_design,
        "suitDesign": "4,000000,000000,000000",
        "helmetDesign": "35,000000,000000,000000",
        "carPath": car_path,
        "carId": car_id,
        "sponsor1": sponsor1,
        "sponsor2": 0,
        "numberDesign": "0,0,FFFFFF,777777,000000",
        "driverSkill": skill,
        "driverAggression": aggression,
        "driverOptimism": optimism,
        "driverSmoothness": smoothness,
        "pitCrewSkill": pit_crew_skill,
        "strategyRiskiness": pit_strategy_riskiness,
        "driverAge": age,
        "id": f"{uuid.uuid4()}",
        "rowIndex": i,
        "carClassId": 0
    }
    drivers.append(driver)

roster = {"drivers": drivers}
roster_json = json.dumps(roster, indent=4)
print(roster_json)

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
file_path = os.path.join(folder_name, "roster.json")
with open(file_path, "w") as f:
    f.write(roster_json)