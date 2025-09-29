import streamlit as st
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="dbs_kafe",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

# --- Login Staff Sederhana ---
st.set_page_config(page_title="Staff Angza", page_icon="🧑‍🍳", layout="wide")
st.title("👨‍🍳 Dashboard Staff Angza Coffeeshop")
st.markdown("---")

img = "https://i.postimg.cc/3xg6i6Zg/Logo-Angza-Coffeeshop-1.jpg"
st.image(img, use_container_width=True, output_format="JPEG", caption="Angza Coffeeshop")

if "login" not in st.session_state:
    st.session_state.login = False

def check_login(username, password):
    # Username dan password bisa diganti sesuai kebutuhan
    return username == "staff" and password == "angza123"

if not st.session_state.login:
    with st.form("login_staff"):
        st.subheader("Login Staff")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            if check_login(username, password):
                st.session_state.login = True
                st.success("Login berhasil!")
                st.rerun()
            else:
                st.error("Username atau password salah.")
    st.stop()

# --- Fitur Update Status Pesanan ---
# Pastikan kolom status ada di tabel customer
def ensure_status_column():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SHOW COLUMNS FROM customer LIKE 'status'")
        result = cursor.fetchone()
        if not result:
            cursor.execute("ALTER TABLE customer ADD COLUMN status VARCHAR(20) DEFAULT 'Menunggu'")
    conn.commit()
    conn.close()

ensure_status_column()

# Pastikan kolom waktu ada di tabel customer
def ensure_waktu_column():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SHOW COLUMNS FROM customer LIKE 'waktu'")
        result = cursor.fetchone()
        if not result:
            cursor.execute("ALTER TABLE customer ADD COLUMN waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    conn.commit()
    conn.close()

ensure_waktu_column()

# Pastikan kolom id ada di tabel customer
def ensure_id_column():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SHOW COLUMNS FROM customer LIKE 'id'")
        result = cursor.fetchone()
        if not result:
            cursor.execute("ALTER TABLE customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")
    conn.commit()
    conn.close()

ensure_id_column()

# Tampilkan daftar pesanan terbaru
conn = get_connection()
with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM customer ORDER BY waktu DESC")
    orders = cursor.fetchall()

if not orders:
    st.info("Belum ada pesanan masuk.")
else:
    for order in orders:
        st.markdown(f"""
        <div style="background:#fff0f6; border-radius:12px; box-shadow:0 2px 12px #ffb6c1aa; padding:1em; margin-bottom:1em;">
            <b>Nama:</b> {order['nama']}<br>
            <b>Metode:</b> {order['metode']}<br>
            <b>Daftar Belanja:</b> {order['daftar_belanja']}<br>
            <b>Nominal:</b> {order['nominal']}<br>
            <b>Waktu:</b> {order['waktu']}<br>
            <b>Status:</b> <span style="color:#ff69b4;"><b>{order.get('status', 'Menunggu')}</b></span>
        """, unsafe_allow_html=True)
        # Form update status
        with st.form(f"update_status_{order['id']}"):
            new_status = st.selectbox(
                "Update Status",
                ["Menunggu", "Diproses", "Selesai"],
                index=["Menunggu", "Diproses", "Selesai"].index(order.get('status', 'Menunggu'))
            )
            update = st.form_submit_button("Update Status")
            if update:
                with conn.cursor() as cursor2:
                    cursor2.execute(
                        "UPDATE customer SET status=%s WHERE id=%s",
                        (new_status, order['id'])
                    )
                conn.commit()
                st.success(f"Status pesanan {order['nama']} diperbarui menjadi {new_status}.")
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

conn.close()