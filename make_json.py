import json
from faker import Faker

faker = Faker()

positions_list = [
    "Contractor",
    "Accountant",
    "Games developer",
    "Mechanical engineer",
    "Media planner",
    "Designer",
    "Backend Developer",
    "Frontend Develope",
    "QA",
    "Data processing manager"
]

data = []
for _ in range(50000):
    record = {
        "full_name": faker.name(),
        "date_hired": faker.date_between(start_date='-5y', end_date='today').strftime("%Y-%m-%d"),
        "email": faker.email(),
        "position": faker.job(),
    }
    data.append(record)

with open("employee_data.json", "w") as json_file:
    json.dump(data, json_file)
