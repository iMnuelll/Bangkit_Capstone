from faker import Faker
import random
import pandas as pd
import numpy as np

fake = Faker()

def generate_user_data(productive_time):
    return {
        "name": fake.name(),
        "gender": random.randint(0, 1),
        "age" : random.randint(20, 39),
        "job" : random.randint(0, 5),
        "task" : random.randint(0, 6),
        "work_days" : random.randint(1, 7),
        "difficulty" : random.randint(1, 5),
        "average_work_hour" : round(random.uniform(1.0, 12.5), 1),
        "average_rest" : round(random.uniform(1.0, 4.0), 1),
        "mood_before_work" : random.randint(0, 2),
        "mood_after_work" : random.randint(0, 2),
        "deadline" : random.randint(0, 4),
        "importance" : random.randint(1, 5),
        "sleep_average" : round(random.uniform(1.0, 8.5), 1),
        # "productive_time" : random.randint(0, 3),
        'productive_time' : productive_time,
        "urgency" : random.randint(1, 5),
        "Gangguan dari atasan" : random.randint(0 ,1),    
        "Gangguan dari internal " : random.randint(0 ,1),
        "Gangguan dari kesehatan" : random.randint(0 ,1),
        "Gangguan dari lingkungan sekitar " : random.randint(0 ,1),
        "Gangguan dari perangkat elektronik " : random.randint(0 ,1),
        "Gangguan dari teman atau rekan kerja" : random.randint(0 ,1),
        "Gangguan internet" : random.randint(0 ,1),
        "Mood " : random.randint(0 ,1),
        "Panggilan Telepon" : random.randint(0 ,1),
        "Tidak ada" : random.randint(0 ,1),
        "ajakan bermain" : random.randint(0 ,1)
    }
total_samples = 100

productive_time_values = np.tile(np.arange(4), total_samples // 4)
np.random.shuffle(productive_time_values)

data = []

# Generate data menggunakan nilai productive_time yang telah dihasilkan
for productive_time in productive_time_values:
    data.append(generate_user_data(productive_time))

# Mengonversi data menjadi DataFrame
df = pd.DataFrame(data)

print(df['productive_time'].value_counts())

# Download to csv
df.to_csv('new_data_dummy.csv', index=False)