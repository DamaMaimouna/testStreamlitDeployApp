from faker import Faker
import json
import random
from datetime import datetime, timedelta

# Initialize the Faker generator
fake = Faker()

# Start and end date for generating random dates
start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2024-01-01', '%Y-%m-%d')

# Generate the dataset
dataset = []
for _ in range(100):  # Generate 100 records
    start = fake.date_between(start_date=start_date, end_date=end_date - timedelta(days=7))
    end = start + timedelta(days=7)  # Ensure end date is exactly 7 days after start date
    record = {
        'start_date': start.strftime('%Y-%m-%d'),
        'end_date': end.strftime('%Y-%m-%d'),
        'nbr_validated': random.randint(0, 100),
        'nbr_refused': random.randint(0, 100),
        'timestamp': end.strftime('%Y-%m-%d'),
    }
    dataset.append(record)

# Write data to a JSON file
with open('data/dataset.json', 'w') as f:
    json.dump(dataset, f, indent=4)

print("Dataset generated and written to dataset.json")
