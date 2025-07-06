# Sistem Rekomendasi Trayek Transjakarta
Proyek ini merupakan dashboard interaktif berbasis Streamlit yang digunakan untuk:
1. Monitoring tren kecepatan lalu lintas harian di Jakarta  
2. Prediksi kecepatan harian menggunakan model Machine Learning

---

# Tujuan Proyek

Proyek ini bertujuan untuk membantu memahami dan memantau kondisi lalu lintas di Jakarta melalui:

1. Visualisasi tren kecepatan rata-rata per hari dan ruas jalan, untuk mengidentifikasi waktu dan lokasi yang rawan kemacetan.
2. Prediksi kecepatan harian menggunakan model Machine Learning ringan, agar pengambil keputusan bisa memperkirakan kondisi keesokan hari.
3. Menyediakan alat bantu interaktif berbasis Streamlit yang mudah digunakan oleh pengguna non-teknis, seperti dinas transportasi atau warga umum.

Dengan pendekatan ini, proyek ini menjadi contoh penerapan data science untuk isu kota besar yang nyata dan relevan.

---


# Fitur Utama
* Visualisasi Kecepatan per Hari | Melihat pola kecepatan di setiap hari (Senin–Minggu) |
* Tren per Ruas Jalan | Menampilkan grafik kecepatan harian untuk tiap ruas jalan |
* Top 5 Jalan Paling Padat | Mengurutkan jalan dengan rata-rata kecepatan terendah |
* Heatmap Hari vs Bulan | Menampilkan pola waktu kemacetan (hari & bulan) |
* Prediksi Kecepatan Besok | Prediksi kecepatan hari berikutnya dengan Random Forest |
* Evaluasi Model | Menampilkan akurasi model menggunakan RMSE |

# Instalasi dan Menjalankan
# 1. Clone Repository dan Masuk Folder
```bash
git clone https://github.com/Jo2205/kecepatan-jalan-jakarta.git
cd kecepatan-jalan-jakarta
```

# 2. Install Library
```bash
pip install -r requirements.txt
```

# 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

# Output
Output akhir dari proyek ini berupa dashboard interaktif Streamlit yang memungkinkan pengguna melihat tren kecepatan lalu lintas, menemukan titik kemacetan tertinggi, dan memprediksi kecepatan rata-rata untuk hari berikutnya secara otomatis menggunakan machine learning.

# Contoh Tampilan Aplikasi
(https://github.com/Jo2205/kecepatan-jalan-jakarta/blob/main/output/prediksi.png?raw=true)

