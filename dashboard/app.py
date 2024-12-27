import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk memuat data dengan caching
@st.cache_data  
def load_data():
    day_data = pd.read_csv('../data/day.csv')
    hour_data = pd.read_csv('../data/hour.csv')
    return day_data, hour_data

# Memuat data
day_data, hour_data = load_data()

# Judul Dashboard
st.title('Dashboard Analisis Penyewaan Sepeda')
st.write('Berdasarkan File day.csv dan hour.csv')
st.markdown('---')

# Pengantar
st.markdown("""
Selamat datang di Dashboard Analisis Penyewaan Sepeda. 
Di sini, kita akan menganalisis data penyewaan sepeda untuk menjawab beberapa pertanyaan bisnis utama.
""")

# Pengaturan margin menggunakan custom CSS
st.markdown(
    """
    <style>
    .custom-margin {
        margin-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Pertanyaan Bisnis 1: Bagaimana kondisi cuaca mempengaruhi penyewaan sepeda per jam?
st.header('Bagaimana kondisi cuaca mempengaruhi penyewaan sepeda per jam?')
st.markdown("""
Dalam analisis ini, kita akan melihat bagaimana kondisi cuaca mempengaruhi jumlah penyewaan sepeda per jam.
""")
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(data=hour_data, x='hr', y='cnt', hue='weathersit', ax=ax)
ax.set_title('Penyewaan Sepeda berdasarkan Jam dan Kondisi Cuaca')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Penjelasan hasil visualisasi
st.markdown("""
Dari grafik di atas, kita dapat melihat bahwa kondisi cuaca memiliki dampak yang signifikan terhadap jumlah penyewaan sepeda per jam.
""")

# Menggunakan custom CSS untuk pengaturan margin
st.markdown('<div class="custom-margin"></div>', unsafe_allow_html=True)

# Pertanyaan Bisnis 2: Bagaimana musim mempengaruhi penyewaan sepeda?
st.header('Bagaimana musim mempengaruhi penyewaan sepeda?')
st.markdown("""
Selanjutnya, kita akan melihat bagaimana musim mempengaruhi jumlah penyewaan sepeda.
""")
fig, ax = plt.subplots(figsize=(14, 7))
sns.boxplot(data=day_data, x='season', y='cnt', ax=ax)
ax.set_title('Penyewaan Sepeda berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Penjelasan hasil visualisasi
st.markdown("""
Grafik di atas menunjukkan bahwa jumlah penyewaan sepeda bervariasi tergantung musim. 
Musim semi dan musim panas cenderung memiliki jumlah penyewaan yang lebih tinggi dibandingkan musim gugur dan musim dingin.
""")

# Menggunakan custom CSS untuk pengaturan margin
st.markdown('<div class="custom-margin"></div>', unsafe_allow_html=True)

# Pertanyaan Bisnis Tambahan: Bagaimana tren penyewaan sepeda di hari kerja dan akhir pekan?
st.header('Bagaimana tren penyewaan sepeda di hari kerja dan akhir pekan?')
st.markdown("""
Terakhir, kita akan melihat bagaimana tren penyewaan sepeda bervariasi antara hari kerja dan akhir pekan.
""")
fig, ax = plt.subplots(figsize=(14, 7))
sns.boxplot(data=day_data, x='weekday', y='cnt', ax=ax)
ax.set_title('Penyewaan Sepeda berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Menggunakan custom CSS untuk pengaturan margin
st.markdown('<div class="custom-margin"></div>', unsafe_allow_html=True)

# Kesimpulan
st.header('Kesimpulan')
st.markdown("""
Dari analisis di atas, kita dapat menyimpulkan bahwa kondisi cuaca, musim, dan jenis hari (hari kerja atau akhir pekan) 
berpengaruh signifikan terhadap jumlah penyewaan sepeda. Informasi ini dapat digunakan untuk mengoptimalkan ketersediaan 
sepeda berdasarkan prediksi cuaca dan musim, serta mempersiapkan jumlah sepeda yang lebih banyak pada akhir pekan.
""")
