import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Monitoring & Prediksi Kecepatan Jalan Jakarta")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/kecepatan_ratarata2023.csv')
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df['bulan'] = df['tanggal'].dt.month  # Tetap ambil bulan dari tanggal
    return df

df = load_data()
st.subheader("Contoh Data")
st.dataframe(df.head())

# ======================
# VISUALISASI HARIAN
# ======================
st.subheader("Rata-rata Kecepatan per Hari")

# Hitung rata-rata kecepatan berdasarkan nama hari
rata_per_hari = df.groupby("hari")["kecepatan"].mean().reset_index()

# Urutkan hari secara manual agar urut (Senin–Minggu)
urutan_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
rata_per_hari["hari"] = pd.Categorical(rata_per_hari["hari"], categories=urutan_hari, ordered=True)
rata_per_hari = rata_per_hari.sort_values("hari")

# Tampilkan dalam bentuk bar chart
st.bar_chart(data=rata_per_hari, x="hari", y="kecepatan")

# ===========================
# GRAFIK TREND PER RUAS JALAN
# ===========================
st.subheader("Tren Kecepatan Harian per Ruas Jalan")

# Bikin dropdown buat pilih nama ruas jalan
daftar_ruas = df["ruas_jalan"].dropna().unique()
ruas_dipilih = st.selectbox("Pilih ruas jalan:", sorted(daftar_ruas))

# Filter data sesuai ruas yang dipilih
df_ruas = df[df["ruas_jalan"] == ruas_dipilih]

# Bikin grafik garis kecepatan harian
st.line_chart(
    data=df_ruas.set_index("tanggal")["kecepatan"],
    use_container_width=True
)

# ===========================
# TOP 5 RUAS JALAN TERSIBUK
# ===========================
st.subheader("Top 5 Ruas Jalan Paling Macet (Rata-rata Kecepatan Terendah)")

# Hitung rata-rata kecepatan per ruas
rata_per_ruas = df.groupby("ruas_jalan")["kecepatan"].mean().reset_index()

# Ambil 5 ruas dengan kecepatan terendah
top5_paling_macet = rata_per_ruas.nsmallest(5, "kecepatan")

# Bikin bar chart
st.bar_chart(data=top5_paling_macet, x="ruas_jalan", y="kecepatan")


# ===========================
# HEATMAP HARI vs BULAN
# ===========================
st.subheader("Heatmap Kecepatan Rata-rata (Hari vs Bulan)")

# Hitung rata-rata kecepatan berdasarkan hari & bulan
pivot_hari_bulan = df.pivot_table(
    index="hari", columns="bulan", values="kecepatan", aggfunc="mean"
)

# Urutkan hari biar bener urut
urutan_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
pivot_hari_bulan = pivot_hari_bulan.reindex(urutan_hari)

# Buat heatmap
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pivot_hari_bulan, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.5, ax=ax)
ax.set_title("Rata-rata Kecepatan (km/jam) per Hari dan Bulan", fontsize=14)
st.pyplot(fig)

# ===========================
# PREDIKSI KECEPATAN BESOK
# ===========================
from utils.modeling import prepare_data, train_model_with_evaluation, predict_besok

st.subheader("Prediksi Kecepatan Besok")

# Pilih ruas jalan untuk diprediksi
ruas_prediksi = st.selectbox("Pilih ruas jalan untuk diprediksi:", sorted(df["ruas_jalan"].unique()), key="prediksi")

# Siapkan data dan fitur prediksi
X, y, df_ruas_full = prepare_data(df, ruas_prediksi)

if len(X) >= 5:  # pastikan datanya cukup untuk split
    # Latih model + evaluasi
    model, rmse = train_model_with_evaluation(X, y)

    # Tanggal besok (simulasi dari data terakhir)
    tanggal_terakhir = df_ruas_full["tanggal"].max()
    tanggal_besok = tanggal_terakhir + pd.Timedelta(days=1)

    # Ambil input fitur terakhir
    last_bulan = df_ruas_full["bulan"].iloc[-1]
    last_rolling = df_ruas_full["rolling_3"].iloc[-1]

    # Lakukan prediksi
    prediksi = predict_besok(model, last_bulan, last_rolling)

    # Tampilkan hasil
    st.success(f"""
    Prediksi kecepatan rata-rata untuk ruas **{ruas_prediksi}** pada tanggal **{tanggal_besok.strftime('%d %B %Y')}**:
    **{prediksi:.2f} km/jam**
    """)

    st.info(f"Evaluasi model (RMSE): {rmse:.2f} km/jam")
else:
    st.warning("Data untuk ruas jalan ini belum cukup untuk melakukan prediksi.")
