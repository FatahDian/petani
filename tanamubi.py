import streamlit as st

# Input dari pengguna
jumlah_tanaman_per_hektar = st.number_input("Jumlah Tanaman per Hektar:", min_value=1, value=1)
jumlah_malai_per_tanaman = st.number_input("Jumlah Malai per Tanaman:", min_value=1, value=1)
berat_bulir_per_malai = st.number_input("Berat Bulir per Malai (kg):", min_value=0.01, value=0.01)
jarak_tanam = st.number_input("Jarak Tanam (cm):", min_value=1, value=20)
jarak_baris = st.number_input("Jarak Baris (cm):", min_value=1, value=30)

# Perhitungan
hasil_panen = jumlah_tanaman_per_hektar * jumlah_malai_per_tanaman * berat_bulir_per_malai
populasi_tumbuhan_per_hektar = jumlah_tanaman_per_hektar / (jarak_tanam / 100) / (jarak_baris / 100)  # Konversi cm ke meter

# Output
st.write(f"Perkiraan Hasil Panen: {hasil_panen:.2f} Ton per Hektar")
st.write(f"Jumlah Populasi Tumbuhan per Hektar: {populasi_tumbuhan_per_hektar:.2f} Tanaman per Hektar")
