from faker import Faker
import random
from datetime import datetime, timedelta
import csv

fake = Faker()

def generate_user_data():
    return {
        "Identitas Pengguna": fake.name(),
        "Mood user": random.choice(["Senang", "Sedih", "Stres", "Bahagia", "Cemas"]),
        "Durasi Tidur": random.randint(4, 10),  # Jam tidur per malam
        "Kondisi Fisik": random.choice(["Sehat", "Sakit"]),
    }

def generate_task_data():
    start_time = fake.date_time_between(start_date="-30d", end_date="now")
    end_time = start_time + timedelta(hours=random.randint(1, 8))
    return {
        "Jam Mulai": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "Jam Selesai" : end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "Durasi Kerja": (end_time - start_time).total_seconds() / 3600,  # Durasi kerja dalam jam
        "Durasi Istirahat": random.randint(0, 2),  # Durasi istirahat dalam jam
        "Jenis Tugas": random.choice(["Kreatif", "Analitis", "Fisik", "Administratif"]),
        "Tingkat Kesulitan Tugas": random.randint(1, 10),
        "Interruptions": random.randint(0, 5),
        "Deadline": (start_time + timedelta(days=random.randint(1, 14))).strftime("%Y-%m-%d"),
        "Urgency": random.randint(1, 5),
        "Importance": random.randint(1, 5)
    }

# Generate data
num_users = 140 #Jumlah User
user_data = [generate_user_data() for _ in range(num_users)]

tasks_per_user = 1 # Jumlah task / tugas user
task_data = []
for user in user_data:
    for i in range(tasks_per_user):
        task = generate_task_data()
        task.update({"Identitas Pengguna": user["Identitas Pengguna"]})
        task_data.append(task)

# Simpan data pengguna ke dalam file CSV
with open('user_data.csv', mode='w', newline='') as file:
    fieldnames_user = ['Identitas Pengguna', 'Mood user', 'Durasi Tidur', 'Kondisi Fisik']
    writer = csv.DictWriter(file, fieldnames=fieldnames_user)

    writer.writeheader()
    for user in user_data:
        writer.writerow(user)

# Simpan data tugas ke dalam file CSV
with open('task_data.csv', mode='w', newline='') as file:
    fieldnames_task = ['Identitas Pengguna', 'Jam Mulai',"Jam Selesai", 'Durasi Kerja', 'Durasi Istirahat', 
                       'Jenis Tugas', 'Tingkat Kesulitan Tugas', 'Interruptions', 
                       'Deadline', 'Urgency', 'Importance']
    writer = csv.DictWriter(file, fieldnames=fieldnames_task)

    writer.writeheader()
    for task in task_data:
        writer.writerow(task)
