# Proyek Analisis Data: Penyewaan Sepeda

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti cuaca, musim, dan waktu dalam sehari. Kami menggunakan dua dataset: `day.csv` untuk data harian dan `hour.csv` untuk data per jam.

## Struktur Direktori
- **dashboard**: Berisi file untuk membuat dashboard dengan Streamlit.
- **data**: Berisi dataset yang digunakan dalam analisis.
- **notebook.ipynb**: Berisi seluruh proses analisis data.
- **requirements.txt**: Berisi daftar library yang digunakan.
- **url.txt** (opsional): Berisi tautan ke dashboard yang telah di-deploy.

## Cara Menjalankan Dashboard
1. Pastikan Anda telah menginstal semua library yang diperlukan dengan menjalankan `pip install -r requirements.txt`.
2. Jalankan file `app.py` dengan perintah `streamlit run app.py`.

## Insight dari Hasil Analisis
1. Kondisi cuaca memiliki dampak signifikan terhadap jumlah penyewaan sepeda per jam.
2. Jumlah penyewaan sepeda bervariasi tergantung musim, dengan musim semi dan musim panas memiliki jumlah penyewaan yang lebih tinggi dibandingkan musim gugur dan musim dingin.
3. Jumlah penyewaan sepeda pada akhir pekan cenderung lebih tinggi dibandingkan hari kerja.

## Penjelasan Dataset
- **day.csv**: Data penyewaan sepeda harian.
- **hour.csv**: Data penyewaan sepeda per jam.

## Library yang Digunakan
- pandas
- seaborn
- matplotlib
- streamlit
