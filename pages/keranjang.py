import streamlit as st
from db import init_db, insert_customer

st.set_page_config(page_title="Keranjang - Angza", page_icon="🛒", layout="wide")

# CSS soft pink & animasi
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #fff0f6 60%, #ffd6e0 100%);
}
.block-container {
    background: #fff0f6;
}
.cart-card {
    background: linear-gradient(135deg, #fff0f6 60%, #ffd6e0 100%);
    border-radius: 18px;
    box-shadow: 0 2px 12px #ffb6c1aa;
    padding: 1.5rem 1rem 1rem 1rem;
    margin-bottom: 1.5rem;
    animation: float 3s ease-in-out infinite;
}
.cart-card img {
    animation: float 3s ease-in-out infinite;
    border-radius: 14px;
    box-shadow: 0 2px 12px #ffb6c1aa;
}
@keyframes float {
    0% { transform: translatey(0px);}
    50% { transform: translatey(-12px);}
    100% { transform: translatey(0px);}
}
.pay-anim {
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 #ffb6c1aa;}
    70% { box-shadow: 0 0 0 12px #ffd6e055;}
    100% { box-shadow: 0 0 0 0 #ffb6c1aa;}
}
.pay-btn button {
    background: linear-gradient(90deg, #ffb6c1 60%, #ffd6e0 100%);
    color: #222;
    border-radius: 8px !important;
    font-weight: bold;
    border: none;
    transition: 0.2s;
}
.pay-btn button:hover {
    background: linear-gradient(90deg, #ffd6e0 60%, #ffb6c1 100%);
    color: #000;
    transform: scale(1.05);
}
hr {
    border: 1px solid #ffd6e0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#ff69b4;">🛒 Keranjang Belanja Anda</h1>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

cart = st.session_state.get("cart", [])

if not cart:
    st.info("Keranjang masih kosong. Silakan pesan produk dari menu.")
else:
    total = 0
    belanjaan = []
    for item in cart:
        st.markdown('<div class="cart-card">', unsafe_allow_html=True)
        st.image(item["gambar"], width=120)
        st.write(f"**{item['nama']}** - {item['harga']}")
        st.write(item["deskripsi"])
        st.markdown('</div>', unsafe_allow_html=True)
        total += int(item["harga"].replace("Rp ", "").replace(".", ""))
        belanjaan.append(item["nama"])
    st.success(f"**Total Belanja: Rp {total:,.0f}**".replace(",", "."))

    if st.button("Kosongkan Keranjang"):
        st.session_state.cart = []
        st.experimental_rerun()

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#ff69b4;">Pembayaran</h2>', unsafe_allow_html=True)
    # Tampilkan daftar belanjaan
    st.markdown("**Daftar Belanjaan:**")
    st.markdown(", ".join(belanjaan))

    with st.form("form_pembayaran"):
        nama = st.text_input("Nama Pemesan")
        metode = st.selectbox(
            "Metode Pembayaran",
            [
                "Tunai 💵",
                "QRIS 🟪",
                "Transfer Bank 🏦"
            ],
            index=1
        )
        # Daftar belanjaan di bawah metode pembayaran
        st.markdown("**Daftar Belanjaan:**")
        st.markdown(", ".join(belanjaan))
        bayar = st.text_input("Nominal Pembayaran (Rp)", value=str(total))
        submit = st.form_submit_button("Bayar Sekarang")
        if submit:
            if not nama or not bayar:
                st.warning("Mohon lengkapi data pembayaran.")
            elif int(bayar.replace(".", "")) < total:
                st.error("Nominal pembayaran kurang dari total belanja.")
            else:
                # Gabungkan nama produk menjadi satu string
                daftar_belanja = ", ".join(belanjaan)
                insert_customer(nama, metode, daftar_belanja, bayar)  # <-- gunakan daftar_belanja
                st.markdown(
                    f"""
                    <div class="pay-anim" style="background:#fff0f6; border-radius:16px; padding:1.5em; margin:1em 0; text-align:center;">
                        <span style="font-size:2em;">🎉</span><br>
                        <span style="color:#ff69b4; font-size:1.2em;">
                        Terima kasih, <b>{nama}</b>!<br>
                        Pembayaran <b>{metode}</b> berhasil.<br>
                        Pesanan Anda: <b>{daftar_belanja}</b><br>
                        Pesanan Anda sedang diproses ☕
                        </span>
                    </div>
                    """, unsafe_allow_html=True
                )
                st.session_state.cart = []

    st.markdown("""
    <div style="text-align:center; margin-top:2em;">
        <span style="color:#ffb6c1;">*Pilih metode pembayaran favoritmu dan nikmati pengalaman belanja di Angza Coffeeshop!*</span>
    </div>
    """, unsafe_allow_html=True)

init_db()  # Pastikan database dan tabel sudah siap