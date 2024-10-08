import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set the page config to use a blue theme
st.set_page_config(page_title="AirWise", layout="wide", initial_sidebar_state="expanded")

# Load the model
model = joblib.load('model_airwise.pkl')

# Function to map numerical predictions to categorical labels
def map_prediction(prediction):
    if prediction == 3:
        return "Baik", (
            "Aman untuk beraktivitas di luar ruangan, namun tetap waspada "
            "terhadap perubahan kondisi. Manfaatkan kesempatan ini untuk berolahraga ringan di luar ruangan. "
            "Jaga pola makan sehat dan seimbang untuk meningkatkan daya tahan tubuh. Jika merasa tidak enak badan, "
            "segera istirahat dan konsultasikan dengan tenaga kesehatan jika diperlukan."
        )
    elif prediction == 2:
        return "Sedang", (
            "Masih aman untuk beraktivitas di luar ruangan, namun siapkan "
            "masker sebagai antisipasi. Perbanyak minum air putih untuk menjaga kesehatan tubuh. "
            "Konsumsi beragam buah dan sayuran segar untuk meningkatkan daya tahan tubuh. "
            "Jika merasa tidak enak badan, segera istirahat dan konsultasikan dengan tenaga kesehatan jika diperlukan."
        )
    elif prediction == 1:
        return "Tidak Sehat", (
            "Kurangi aktivitas di luar ruangan dan gunakan masker "
            "jika harus keluar ruangan. Perbanyak istirahat dan konsumsi makanan bergizi seimbang. "
            "Jaga kebersihan diri dan lingkungan sekitar. Jika mengalami gangguan pernapasan atau "
            "merasa tidak enak badan, segera konsultasikan dengan tenaga kesehatan."
        )
    else:
        return "Sangat Tidak Sehat", (
            "Hindari kegiatan di luar ruangan dan selalu gunakan "
            "masker jika terpaksa keluar ruangan. Perbanyak minum air putih dan istirahat yang cukup. "
            "Konsumsi makanan bergizi seimbang untuk menjaga daya tahan tubuh. Pertimbangkan penggunaan air purifier "
            "agar kualitas udara di dalam ruangan tetap baik. Jika mengalami gangguan kesehatan, segera dapatkan "
            "bantuan medis."
        )

# Title of the web app
st.title('AirWise: Prediksi Kualitas Udara :cloud: :sunny:')

# Subtitle to raise awareness
st.write("""
Pemantauan kualitas udara sangat penting untuk mencegah Infeksi Saluran Pernapasan Akut (ISPA). 
Udara yang tercemar dapat meningkatkan risiko ISPA dan memperburuk gejala yang ada. 
Gunakan AirWise untuk mengetahui status kualitas udara di sekitar Anda dan ambil tindakan pencegahan yang tepat.
""")

st.write("""
**Waspadai gejala-gejala berikut yang mungkin menandakan ISPA:**

1. Batuk
2. Hidung Tersumbat
3. Sakit Tenggorokan
4. Demam
5. Sesak Napas
6. Sakit Kepala
7. Nyeri Otot dan Sendi
8. Lemas atau Lelah
9. Suara Serak atau Hilangnya Suara 
10. Pilek atau Nyeri Sinus
11. Mual, Muntah, atau Diare
12. Nafsu Makan Menurun

**Jika Anda mengalami beberapa gejala di atas, segera konsultasikan dengan tenaga medis.**
""")

# Input fields for the features
pm10 = st.number_input("PM10 (Particulate Matter Sampai 10 Mikrometer)", min_value=0, max_value=1000, value=50, step=1)
pm25 = st.number_input("PM2.5 (Particulate Matter Sampai 2.5 Mikrometer)", min_value=0, max_value=1000, value=25, step=1)
so2 = st.number_input("SO₂ (Sulfur Dioksida)", min_value=0, max_value=1000, value=10, step=1)
co = st.number_input("CO (Karbon Monoksida)", min_value=0, max_value=1000, value=10, step=1)
o3 = st.number_input("O₃ (Ozon)", min_value=0, max_value=1000, value=100, step=1)
no2 = st.number_input("NO₂ (Nitrogen Dioksida)", min_value=0, max_value=1000, value=20, step=1)

# Button for prediction
if st.button("Prediksi Kualitas Udara"):
    # Prepare the input data
    input_data = pd.DataFrame({
        'pm10': [pm10],
        'pm25': [pm25],
        'so2': [so2],
        'co': [co],
        'o3': [o3],
        'no2': [no2]
    })

    # Make the prediction
    prediction = model.predict(input_data)[0]

    # Map the prediction to the categorical label
    label, description = map_prediction(prediction)

    # Display the result
    st.write(f"Kualitas Udara: {label}")
    st.write(description)
