import pymysql

def get_connection():
    return pymysql.connect(
        host="aws-1-ap-southeast-1.pooler.supabase.com",
        user="postgres.snmldvihylobnakviqpj",
        password="angza123",
        database="postgres",
        cursorclass=pymysql.cursors.DictCursor
    )

def init_db():
    # Membuat database jika belum ada
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS dbs_kafe")
    conn.select_db("dbs_kafe")
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(50) NOT NULL,
                metode VARCHAR(50) NOT NULL,
                daftar_belanja VARCHAR(50) NOT NULL,
                nominal VARCHAR(50) NOT NULL,
                waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    conn.close()

def insert_customer(nama, metode, daftar_belanja, nominal):
    conn = get_connection()
    conn.select_db("dbs_kafe")
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO customer (nama, metode, daftar_belanja, nominal) VALUES (%s, %s, %s, %s)",
            (nama, metode, daftar_belanja, nominal)
        )
    conn.commit()
    conn.close()