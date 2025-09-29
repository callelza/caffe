import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Angza Coffeeshop",
    page_icon="☕",
    layout="wide"
)

# CSS untuk tema soft pink & animasi gambar
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #fff0f6 60%, #ffd6e0 100%);
}
.block-container {
    background: #fff0f6;
}
hr {
    border: 1px solid #ffd6e0;
}
</style>
""", unsafe_allow_html=True)

# Banner dengan animasi (gunakan class animated-img)
img = Image.open("c:\\angza_coffeshop\\ftoo.jpeg")
st.image(img, use_container_width=True, output_format="JPEG", caption="Angza Coffeeshop")
st.markdown(
    """
    <style>
    .element-container img {
        border-radius: 18px;
        box-shadow: 0 4px 24px #ffb6c1aa;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translatey(0px);}
        50% { transform: translatey(-18px);}
        100% { transform: translatey(0px);}
    }
    </style>
    """, unsafe_allow_html=True
)
st.markdown('<h1 style="text-align:center; color:#ff69b4;">🌟 Selamat Datang di Angza Coffeeshop! 🌟</h1>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Deskripsi singkat dengan dua kolom
col1, col2 = st.columns(2)
with col1:
    st.markdown('<h2 style="color:#ff69b4;">Tentang Kami</h2>', unsafe_allow_html=True)
    st.write("""
    Angza adalah coffeeshop cozy di pusat kota, menyajikan kopi premium 
    dari biji lokal terbaik. Nikmati suasana hangat sambil bekerja atau 
    bersantai dengan teman. Kami buka setiap hari dari pukul 07:00 - 22:00.
    """)

with col2:
    st.markdown('<h2 style="color:#ff69b4;">Jam Buka</h2>', unsafe_allow_html=True)
    st.write("**Senin - Minggu:** 07:00 - 22:00")
    st.write("**Alamat:** Jl. Sudirman No. 123, Jambi")
    st.write("**Telepon:** +62 21 88386075")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<h3 style="color:#ff69b4;">Lihat Menu Kami</h3>', unsafe_allow_html=True)
if st.button("🍰 Ke Menu Produk"):
    st.switch_page("pages/menu.py")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; color:#ffb6c1;'>Copyright © 2025 Angza Coffeeshop</div>",
    unsafe_allow_html=True
)
