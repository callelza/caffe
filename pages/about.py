import streamlit as st
from PIL import Image

st.set_page_config(page_title="Tentang - Angza", page_icon="☕", layout="wide")

# CSS soft pink & animasi gambar
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #fff0f6 60%, #ffd6e0 100%);
}
.block-container {
    background: #fff0f6;
}
.animated-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 18px;
    box-shadow: 0 4px 24px #ffb6c1aa;
    width: 80%;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translatey(0px);}
    50% { transform: translatey(-18px);}
    100% { transform: translatey(0px);}
}
hr {
    border: 1px solid #ffd6e0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#ff69b4;">👋 Tentang Angza Coffeeshop</h1>', unsafe_allow_html=True)

# Gambar dengan animasi
img = Image.open("ftocfe.png")
st.image(img, use_container_width=True, caption="Lokasi Cozy Kami")
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
st.markdown('<div style="text-align:center; color:#ff69b4; font-size:1.1em;">Lokasi Cozy Kami</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Konten tentang
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h2 style="color:#ff69b4;">Sejarah Kami</h2>', unsafe_allow_html=True)
    st.write("""
    Angza Coffeeshop berdiri sejak 2020, lahir dari kecintaan kami terhadap kopi dan suasana hangat. 
    Kami percaya setiap cangkir kopi punya cerita, dan kami ingin membagikan pengalaman itu kepada Anda.
    Biji kopi kami dipilih langsung dari petani lokal terbaik di Jawa Barat dan dipanggang segar setiap minggu.
    """)

with col2:
    st.markdown('<h2 style="color:#ff69b4;">Visi & Daya Tarik</h2>', unsafe_allow_html=True)
    st.write("""
    Kami ingin menjadi destinasi utama pecinta kopi dan komunitas kreatif di kota ini.
    Angza menghadirkan:
    - ☕ **Kopi premium & camilan homemade**
    - 🎶 Musik akustik live setiap akhir pekan
    - 💻 Area kerja nyaman & WiFi super cepat
    - 🌿 Ruang terbuka hijau & interior instagramable
    - 🤝 Event komunitas & workshop rutin
    Rasakan atmosfer yang ramah, penuh inspirasi, dan selalu membuat Anda ingin kembali lagi!
    """)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<h3 style="color:#ff69b4;">Tim Kami</h3>', unsafe_allow_html=True)
st.write("""
Tim Angza terdiri dari barista berpengalaman, chef kreatif, dan staf ramah yang siap menyambut Anda seperti keluarga sendiri.
""")

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align:center; color:#ffb6c1;">*Hubungi kami untuk kemitraan, event, atau saran. Angza, lebih dari sekadar kopi!*</div>',
    unsafe_allow_html=True
)