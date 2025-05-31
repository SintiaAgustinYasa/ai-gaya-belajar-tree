from sklearn.tree import DecisionTreeClassifier

# Dataset latih (contoh): [Visual, Auditori, Kinestetik]
X = [
    [18, 7, 5],   # Visual dominan
    [16, 6, 6],   # Visual dominan
    [5, 16, 6],   # Auditori dominan
    [6, 18, 5],   # Auditori dominan
    [6, 5, 17],   # Kinestetik dominan
    [7, 6, 18],   # Kinestetik dominan
    [14, 10, 6],  # Visual dominan
    [8, 13, 9],   # Auditori dominan
    [9, 7, 14],   # Kinestetik dominan
]

# Label target sesuai data latih
y = [
    "Visual",
    "Visual",
    "Auditori",
    "Auditori",
    "Kinestetik",
    "Kinestetik",
    "Visual",
    "Auditori",
    "Kinestetik"
]

# Membuat dan melatih model Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Kuisioner (10 pertanyaan)
questions = [
    "Saya lebih mudah memahami informasi dalam bentuk gambar, grafik, atau diagram.",
    "Saya suka mencatat dengan warna atau membuat mind map saat belajar.",
    "Saya lebih suka membaca buku yang memiliki gambar atau ilustrasi.",
    "Saya dapat dengan mudah mengingat sesuatu yang saya lihat.",
    "Saya lebih cepat mengerti jika mendengarkan penjelasan dibanding membaca sendiri.",
    "Saya suka belajar dengan cara berdiskusi atau mendengarkan rekaman suara.",
    "Saya sering mengulang-ulang informasi dengan cara membacanya keras-keras.",
    "Saya suka belajar sambil melakukan praktik langsung.",
    "Saya mudah bosan jika hanya duduk diam terlalu lama saat belajar.",
    "Saya memahami materi lebih baik saat ada aktivitas fisik atau simulasi."
]

print("\nJawab pertanyaan berikut dengan angka 1 (Sangat Tidak Setuju) sampai 5 (Sangat Setuju)\n")

visual = auditori = kinestetik = 0

for i, q in enumerate(questions):
    while True:
        try:
            score = int(input(f"{i+1}. {q} (1-5): "))
            if 1 <= score <= 5:
                if i < 4:
                    visual += score
                elif i < 7:
                    auditori += score
                else:
                    kinestetik += score
                break
            else:
                print("Masukkan angka antara 1 hingga 5.")
        except ValueError:
            print("Input tidak valid. Harus berupa angka 1 sampai 5.")

# Prediksi menggunakan model
prediction = model.predict([[visual, auditori, kinestetik]])[0]

# Tips sesuai gaya belajar
tips = {
    "Visual": "Gunakan gambar, warna, diagram, dan mindmap saat belajar.",
    "Auditori": "Belajar sambil mendengarkan, berdiskusi, atau mengajar orang lain.",
    "Kinestetik": "Belajar sambil praktik, menggunakan alat peraga atau bergerak."
}

# Output hasil
print("\n=== HASIL ANALISIS GAYA BELAJAR ===")
print(f"Skor Visual    : {visual}")
print(f"Skor Auditori  : {auditori}")
print(f"Skor Kinestetik: {kinestetik}")
print(f"\nGaya Belajar Dominan Anda: {prediction}")
print(f"Tips Belajar: {tips[prediction]}")