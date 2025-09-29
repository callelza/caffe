import streamlit as st

# --- Styling CSS ---
st.markdown("""
<style>
.product-card {
    background: linear-gradient(135deg, #fff0f6 60%, #ffd6e0 100%);
    border-radius: 18px;
    box-shadow: 0 2px 12px #0001;
    padding: 1.5rem 1rem 1rem 1rem;
    margin-bottom: 1.5rem;
    transition: box-shadow 0.2s;
}
.product-card:hover {
    box-shadow: 0 4px 24px #0002;
}
.price-badge {
    background: #ff69b4;
    color: #fff;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.3em 1em;
    font-size: 1.1em;
    margin-top: 0.5em;
    display: inline-block;
}
.pesan-btn button {
    background: linear-gradient(90deg, #ffb6c1 60%, #ffd6e0 100%);
    color: #222;
    border-radius: 8px !important;
    font-weight: bold;
    border: none;
    transition: 0.2s;
}
.pesan-btn button:hover {
    background: linear-gradient(90deg, #ffd6e0 60%, #ffb6c1 100%);
    color: #000;
    transform: scale(1.05);
}
.product-card img {
    animation: float 3s ease-in-out infinite;
    border-radius: 14px;
    box-shadow: 0 2px 12px #ffb6c1aa;
}
@keyframes float {
    0% { transform: translatey(0px);}
    50% { transform: translatey(-12px);}
    100% { transform: translatey(0px);}
}
</style>
""", unsafe_allow_html=True)

# --- Header halaman ---
st.set_page_config(page_title="Menu - Angza", page_icon="☕", layout="wide")
st.title("☕ Menu Produk Angza Coffeeshop ☕")
st.markdown("---")
st.write("""
Nikmati pilihan kopi dan camilan segar kami. Harga sudah termasuk pajak.  
Pilih kategori di sidebar atau gunakan fitur pencarian.
""")

# --- Sidebar: kategori, pencarian, keranjang ---
st.sidebar.title("Kategori & Fitur")
selected_category = st.sidebar.selectbox(
    "Pilih Kategori:",
    ["Semua", "Kopi", "Makanan"]
)
search_query = st.sidebar.text_input("Cari produk...", "")

if "cart" not in st.session_state:
    st.session_state.cart = []

st.sidebar.markdown(f"**🛒 Keranjang:** {len(st.session_state.cart)} item")
if st.sidebar.button("Lihat Keranjang"):
    st.switch_page("pages/keranjang.py")

# --- Data produk ---
products = {
    "Minuman": [
        {"nama": "Espresso", "harga": "Rp 25.000", "deskripsi": "Kopi hitam pekat, 30ml shot.", "gambar": "esp.avif"},
        {"nama": "Cappuccino", "harga": "Rp 35.000", "deskripsi": "Espresso dengan susu hangat dan busa.", "gambar": "cp.jpg"},
        {"nama": "Latte", "harga": "Rp 40.000", "deskripsi": "Espresso dengan susu steamed, topping foam.", "gambar": "late.jpg"},
        {"nama": "Gulala Sky" , "harga": "Rp 45.000", "deskripsi": "lemon segar, susu, soda, dan es batu.", "gambar": "gl.jpg"},
    ],
    "Makanan": [
        {"nama": "Croissant", "harga": "Rp 20.000", "deskripsi": "Roti lapis renyah dengan mentega asli.", "gambar": "cro.jpg"},
        {"nama": "Cheese Cake", "harga": "Rp 30.000", "deskripsi": "Kue keju lembut dengan topping buah.", "gambar": "csc.jpg"},
        {"nama": "Sandwich Ayam", "harga": "Rp 35.000", "deskripsi": "Sandwich hangat dengan ayam grill dan sayur.", "gambar": "sa.jpg"}
    ],
    "cemilan": [
        {"nama": "Kentang Goreng", "harga": "Rp 15.000", "deskripsi": "Kentang goreng renyah dengan saus sambal.", "gambar": "kt.jpg"},
        {"nama": "waffle", "harga": "Rp 25.000", "deskripsi": "Waffle manis dengan topping coklat dan stroberi.", "gambar": "wf.jpg"},
        {"nama": "pudding", "harga": "Rp 20.000", "deskripsi": "Puding lembut dengan saus karamel dan stroberi.", "gambar": "pd.jpg"}

    ]
}

# --- Fungsi tampil produk ---
def display_products(category, search=""):
    filtered = []
    if category == "Semua":
        for cat in products:
            for item in products[cat]:
                if search.lower() in item["nama"].lower():
                    filtered.append((cat, item))
    else:
        for item in products.get(category, []):
            if search.lower() in item["nama"].lower():
                filtered.append((category, item))

    if not filtered:
        st.info("Produk tidak ditemukan.")
        return

    cols = st.columns(2)
    for idx, (cat, item) in enumerate(filtered):
        with cols[idx % 2]:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(item["gambar"], width=220)
            st.markdown(f"### {item['nama']}")
            st.write(item["deskripsi"])
            st.markdown(f'<span class="price-badge">{item["harga"]}</span>', unsafe_allow_html=True)
            with st.container():
                btn_key = f"pesan_{cat}_{item['nama']}"
                if st.button("Pesan", key=btn_key, help="Tambah ke keranjang", use_container_width=True):
                    st.session_state.cart.append(item)
                    st.success(f"{item['nama']} ditambahkan ke keranjang!")
            st.markdown('</div>', unsafe_allow_html=True)

# --- Tampilkan produk ---
display_products(selected_category, search_query)

# --- Footer ---
st.markdown("---")
st.write(
    "<span style='color:#888'>*Scroll ke atas untuk memilih kategori atau cari produk favoritmu!*</span>",
    unsafe_allow_html=True,
)