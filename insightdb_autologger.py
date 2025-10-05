import psycopg2
import psutil
import time
from datetime import datetime
from faker import Faker

# -------------------------------------
# DATABASE CONFIGURATION
# -------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "database": "metrics",      # ✅ database name
    "user": "postgres",
    "password": "postgres"      # ✅  password
}

# -------------------------------------
# CONNECT TO DATABASE
# -------------------------------------
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# -------------------------------------
# INITIALIZE TABLES IF NOT EXIST
# -------------------------------------
def initialize_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Create system metrics table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS system_metrics (
            id SERIAL PRIMARY KEY,
            recorded_at TIMESTAMP NOT NULL,
            cpu_usage NUMERIC(5,2),
            ram_usage NUMERIC(5,2),
            uptime BIGINT
        );
    """)

    # Create web visitors table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS web_visitors (
            id SERIAL PRIMARY KEY,
            visited_at TIMESTAMP NOT NULL,
            ip_address VARCHAR(50),
            device VARCHAR(500),       -- ✅ increased size to avoid truncation
            referrer VARCHAR(200)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

# -------------------------------------
# INSERT SYSTEM METRICS
# -------------------------------------
def insert_system_metrics():
    conn = get_connection()
    cur = conn.cursor()
    uptime = int(time.time())
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    now = datetime.now()

    cur.execute("""
        INSERT INTO system_metrics (recorded_at, cpu_usage, ram_usage, uptime)
        VALUES (%s, %s, %s, %s);
    """, (now, cpu, ram, uptime))

    conn.commit()
    cur.close()
    conn.close()

# -------------------------------------
# INSERT FAKE WEB VISITOR
# -------------------------------------
def insert_fake_web_visitor():
    conn = get_connection()
    cur = conn.cursor()
    fake = Faker()

    ip = fake.ipv4()
    device = fake.user_agent()[:490]    # ✅ trim to max 490 chars
    referrer = fake.url()[:200]         # ✅ trim to max 200 chars
    now = datetime.now()

    cur.execute("""
        INSERT INTO web_visitors (visited_at, ip_address, device, referrer)
        VALUES (%s, %s, %s, %s);
    """, (now, ip, device, referrer))

    conn.commit()
    cur.close()
    conn.close()

# -------------------------------------
# MAIN LOOP
# -------------------------------------
if __name__ == "__main__":
    print("🚀 InsightDB Auto Logger Started — collecting live data every 60 seconds...")

    # Initialize tables
    initialize_tables()

    while True:
        try:
            insert_system_metrics()
            insert_fake_web_visitor()
            print(f"[{datetime.now().strftime('%H:%M:%S')}] System -> CPU:{psutil.cpu_percent()}% RAM:{psutil.virtual_memory().percent}%")
            time.sleep(60)
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(10)
