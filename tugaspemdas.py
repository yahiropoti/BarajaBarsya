import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2:
print("DataFrame setelah peningkatan 5% gaji:")
print(df)
print("\nRingkasan perubahan:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%.")

# Pertanyaan 3
df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)

# Pertanyaan 4:
print("\nDataFrame setelah peningkatan tambahan untuk usia di atas 30 tahun:")
print(df)
print("\nRingkasan hasil perubahan:")
print("Gaji karyawan di atas 30 tahun ditingkatkan sebesar 2%.")