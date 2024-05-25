import pandas as pd

# Definisikan encoding awal
encoding = {
    "gender": {"Laki-laki": 0, "Perempuan": 1},
    "job": {"Pegawai/Pekerja kantoran": 0, "Siswa/Mahasiswa": 1, "Pengusaha": 2, "Buruh": 3}
}

# Contoh DataFrame dengan pekerjaan yang tidak ada dalam encoding
data = {
    "name": ["Alice", "Bob", "Charlie", "Dave"],
    "gender": ["Perempuan", "Laki-laki", "Laki-laki", "Perempuan"],
    "job": ["Siswa/Mahasiswa", "Pegawai/Pekerja kantoran", "Freelancer", "Buruh"]
}
df = pd.DataFrame(data)

# Variabel untuk menyimpan encoding pekerjaan baru
new_job_id = max(encoding["job"].values()) + 1

# Fungsi untuk melakukan encoding
def encode_job(job):
    global new_job_id
    if job not in encoding["job"]:
        encoding["job"][job] = new_job_id
        new_job_id += 1
    return encoding["job"][job]

# Lakukan encoding pada kolom 'job'
df['job_encoded'] = df['job'].apply(encode_job)

# Lakukan encoding pada kolom 'gender'
df['gender_encoded'] = df['gender'].map(encoding["gender"])

print("DataFrame setelah encoding:")
print(df)

print("\nEncoding yang diperbarui:")
print(encoding)
