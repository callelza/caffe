import streamlit as st

st.set_page_config(page_title="Kontak - Angza", page_icon="📞", layout="wide")

# CSS tema soft pink & hover icon
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #fff0f6 60%, #ffd6e0 100%);
}
.contact-card {
    background: #fff0f6;
    border-radius: 18px;
    box-shadow: 0 2px 12px #ffb6c1aa;
    padding: 2rem;
    margin: 2rem auto;
    max-width: 500px;
    text-align: center;
}
.socmed-icon {
    display: inline-block;
    margin: 0 18px;
    transition: transform 0.2s;
}
.socmed-icon:hover {
    transform: scale(1.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="contact-card">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#ff69b4;">Hubungi Kami</h2>', unsafe_allow_html=True)
st.write("Kami siap melayani pertanyaan, kritik, dan saran Anda.")

st.write("**Alamat:** Jl. Sudirman No. 123, Jambi")
st.write("**Telepon:** +62 21 88386075")
st.write("**Email:** angzacoffee@email.com")

st.markdown('<h3 style="color:#ff69b4;">Sosial Media</h3>', unsafe_allow_html=True)
st.markdown("""
<a href="https://wa.me/622388386075" target="_blank" class="socmed-icon" title="WhatsApp">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/whatsapp.svg" width="48" style="filter: drop-shadow(0 2px 6px #25d36655);" />
</a>
<a href="https://www.instagram.com/callelza_/?igsh=MzNwaGg0M2Rpbjdj&utm_source=qr#" target="_blank" class="socmed-icon" title="Instagram">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/instagram.svg" width="48" style="filter: drop-shadow(0 2px 6px #e1306c55);" />
</a>
<a href="https://tiktok.com/@angzacoffee" target="_blank" class="socmed-icon" title="TikTok">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/tiktok.svg" width="48" style="filter: drop-shadow(0 2px 6px #00000055);" />
</a>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)